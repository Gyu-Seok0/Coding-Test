import os
import copy
import numpy as np
import pandas as pd
import copy
import cv2
from PIL import Image
#from multiprocessing import Pool
import pdb

import torch
from torch.multiprocessing import Pool
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms

from models import *

from openslide import OpenSlide
from tqdm import tqdm
import argparse


def make_otsu_mask(slide, dim):
    thumb = slide.get_thumbnail(dim)
    thumb = np.array(thumb.convert('YCbCr'))
    ret1, th1 = cv2.threshold(thumb[:, :, 1], 16, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret2, th2 = cv2.threshold(thumb[:, :, 2], 16, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    del thumb
    th = th1 | th2
    del th1, th2
    kernel = np.ones((15, 15), np.uint8)
    th = cv2.erode(cv2.dilate(th, kernel, iterations=1), kernel, iterations=1)
    th = cv2.dilate(cv2.erode(th, kernel, iterations=1), kernel, iterations=1)

    return th


def make_patch(args, slide, otsu_index, mag, mpp, tif):
    # make otsu mask
    otsu_mask = make_otsu_mask(slide, slide.level_dimensions[otsu_index])
    # set hyperparameter
    if mag == 400:
        ratio = args.mpp / mpp
        s_ratio = 4
    else:
        ratio = 2 * args.mpp / mpp
        s_ratio = 2
    s = args.size
    # extract coordinates from otsu_mask
    otsu_mask = cv2.resize(otsu_mask, dsize=None, fx=(1./s), fy=(1./s), interpolation=cv2.INTER_AREA)
    otsu_mask = (otsu_mask > 0).astype('uint8')*255
    otsu_mask = cv2.dilate(otsu_mask, np.ones((3, 3), np.uint8), iterations=1)
    coord_list = list(np.argwhere(otsu_mask==255) * s * s_ratio)
    # extract patches from coordinates list
    mp_input_list = [(tif, coord_list[i::os.cpu_count()], s, ratio, s_ratio) for
                     i in range(os.cpu_count())]
    with Pool(os.cpu_count()) as p:
        result = p.starmap(make_patch_each, mp_input_list)
        result = list(zip(*result))
    highr, lowr, coord = [], [], []
    for i in range(os.cpu_count()):
        highr += result[0][i]
        lowr += result[1][i]
        coord += result[2][i]

    return highr, lowr, coord


def make_patch_each(tif, coord_list, s, ratio, s_ratio):
    slide = OpenSlide(tif)
    pad = ((s*3)//2)*s_ratio
    highr_list, lowr_list, coord = [], [], []
    for idx, (y, x) in tqdm(enumerate(coord_list)):
        highr_patch = slide.read_region((int(x), int(y)),
                                        0,
                                        (round(s*ratio*s_ratio), round(s*ratio*s_ratio))
                                        ).convert('RGB').resize((s, s))
        highr_patch = transforms.ToTensor()(highr_patch)
        lowr_patch = slide.read_region((int(x*s)-pad, int(y*s)-pad),
                                       0,
                                       (round(s*ratio*s_ratio*4), round(s*ratio*s_ratio*4))
                                       ).convert('RGB').resize((s, s))
        lowr_patch = transforms.ToTensor()(lowr_patch)
        highr_list.append(highr_patch)
        lowr_list.append(lowr_patch)
        coord.append((y, x))

    return (highr_list, lowr_list, coord)


def main(args):
    # read slide list
    torch.multiprocessing.set_sharing_strategy('file_system')
    sample = args.target_tif
    label = args.target_label
    for root, dirs, files in os.walk(args.target):
        for f in files:
            if f.endswith('tif'):
                if f.split('.')[0] in sample:
                    tif = os.path.join(root, f)
            else:
                continue
    pair_list = []
    # prepare model
    model = MultiRNet(1)
    model.train(False)
    checkpoint = torch.load(args.checkpoint)
    model.load_state_dict(checkpoint['model_state'])
    del checkpoint
    model = torch.nn.DataParallel(model.cuda(), device_ids=range(8))
    cudnn.benchmark = False
    final_dict = {}
    final_dict['slide'] = []
    final_dict['label'] = []
    final_dict['tissue_area'] = []
    final_dict['adeno_area'] = []
    final_dict['max_adeno'] = []
    final_dict['ratio'] = []
    # extract slide feature
    slide = OpenSlide(tif)
    try:
        mpp = float(slide.properties['openslide.comment'].split('MPP=')[-1])
    except:
        return -1
    def_mpp = 0.240
    if def_mpp+0.02 >= mpp >= def_mpp:
        mag = 400
    elif (def_mpp+0.02)*2 >= mpp >= def_mpp*2:
        mag = 200
    elif (def_mpp+0.02)*4 >= mpp >= def_mpp*4:
        mag = 100
    else:
        return -1
    level_scale = [int(i) for i in slide.level_downsamples]
    otsu_scale = mag // args.otsur
    if not otsu_scale in level_scale:
        otsu_index = 0
    else:
        otsu_index = level_scale.index(otsu_scale)
    # extract patch
    highr_patch, lowr_patch, coord_list = make_patch(args, slide, otsu_index, mag, mpp, tif)
    # predict the slide
    if len(highr_patch) == 0:
        return -1
    if (len(highr_patch)//args.batch_size)*args.batch_size == len(highr_patch):
        alpha = 0
    else:
        alpha = 1
    highr_patch = [torch.stack(highr_patch[i*args.batch_size:(i+1)*args.batch_size], dim=0)
                    for i in range(len(highr_patch)//args.batch_size + alpha)]
    lowr_patch = [torch.stack(lowr_patch[i*args.batch_size:(i+1)*args.batch_size], dim=0)
                    for i in range(len(lowr_patch)//args.batch_size + alpha)]
    coord_list = [coord_list[i*args.batch_size:(i+1)*args.batch_size] 
                    for i in range(len(coord_list)//args.batch_size + alpha)]
    output_list = []
    with torch.no_grad():
        for i in range(len(highr_patch)):
            patch1 = highr_patch[i].type_as(torch.cuda.FloatTensor()).cuda()
            patch2 = lowr_patch[i].type_as(torch.cuda.FloatTensor()).cuda()
            output = model(patch1, patch2)
            output_list.extend(list(output.cpu().data.numpy()))
            print(f'{i}/{len(highr_patch)}')
    del highr_patch, lowr_patch, patch1, patch2, output
    torch.cuda.empty_cache()
    # save output
    total_tissue_area = len(output_list)
    total_adeno_area = sum(np.array(output_list) > 0.355)[0]
    max_adeno_output = max(output_list)[0]
    ratio = float(total_adeno_area) / total_tissue_area
    # calculate feature
    final_dict['slide'].append(sample)
    final_dict['label'].append(label)
    final_dict['tissue_area'].append(total_tissue_area)
    final_dict['adeno_area'].append(total_adeno_area)
    final_dict['max_adeno'].append(max_adeno_output)
    final_dict['ratio'].append(ratio)
    # save results
    final_df = pd.DataFrame.from_dict(final_dict)
    if not os.path.exists(args.save):
        os.makedirs(args.save)
    final_df.to_csv(f'{args.save}/{sample}.csv', index=False)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mpp', '-m', default=0.240, type=float)
    parser.add_argument('--size', '-si', default=256, type=int)
    parser.add_argument('--target', '-t', default=None, type=str)
    parser.add_argument('--save', '-s', default='slide_feat', type=str)
    parser.add_argument('--target_tif', '-tf', default=None, type=str)
    parser.add_argument('--target_label', '-tl', default=None, type=str)
    parser.add_argument('--checkpoint', '-cp', default='/nfs/parker/ext01/shared/NIA/nia_checkpoint/model.best.pth.tar', type=str)
    parser.add_argument('--otsur', '-o', default=100, type=int)
    parser.add_argument('--batch_size', '-b', default=256, type=int)

    args = parser.parse_args()
    main(args)
