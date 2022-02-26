import collections
import random

random.seed(1000)

temp = []
for _ in range(10):
    temp.append(random.choice(range(6)))
print(collections.Counter(temp))

order_dict = collections.OrderedDict({'a':1, 'b':2, 'c':3}) # 원래 DICT가 순서대로 안들어왔는데, 이걸 하게되면 순서를 지킬 수 있음.
print(order_dict)

order_dict['aa'] = 4
print(order_dict)