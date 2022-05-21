w#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
data = r.json()

def clean_data(data):
  if (isinstance(data, dict)):
    to_be_deleted = []
    for k in data:
      if (isinstance(data, dict)):
        new_val = clean_data(data[k])
        data[k] = new_val
      if (isinstance(data[k], list)):
        new_val = clean_data(data[k])
        data[k] = new_val
      elif (isinstance(data[k], str)):
        if(data[k] == 'N/A' or data[k] == '-' or data[k] == ''):
          to_be_deleted.append(k)
        
    for i in to_be_deleted:
      del data[i]
    return data

    if (isinstance(data,list)):
      to_be_deleted = []
      for i in range(len(data)):
        if (isinstance(data[i], dict)):
          new_val = clean_data(data[i])
          data[i] = new_val
        
        if (isinstance(data[i],list)):
          new_val = clean_data(data[k])
          data[i] = new_val
        
        elif (isinstance(data[i], str)):
          if (data[i] == 'N/A' or data[i] == '-' or data[i] == ''):
            to_be_deleted.append(i)
      for i in to_be_deleted:
        del data[i]
    return data

print(clean_data(data))


# In[1]:


'a'.isalpha()


# In[4]:


'A B'.lower().split()


# In[5]:


'a'.upper()


# In[27]:


import requests
import numpy as np
import pandas as pd
import json
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))


# In[28]:


d = json.loads(r.text)


# In[42]:


cnt = 0
for item in d["data"].split():
    if item[:3] == "age":
        age = item[4:]
        age = age.replace(",","")
        if int(age) >= 50:
            cnt += 1
print(cnt)


# In[26]:


d[i]


# In[18]:


import requests
import json

def clean(data):
  for i in list(data):
    v = data[i]
    if type(v) == dict:
      clean(v)
    if type(v) == list:
      if '' in v:
        v.remove('')
      elif '-' in v:
        v.remove('-')
      elif 'N/A' in v:
        v.remove('N/A')
    if type(v) == str:
      if v in ['N/A', '', '-']:
        data.pop(i)

def clean_data():
  r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  print(json.dumps(r.json()))
  d = json.loads(r.text)
  clean(d)
  return json.dumps(d)


# In[19]:


r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
print(json.dumps(r.json()))
d = json.loads(r.text)


# In[21]:


d['age']


# In[53]:


test = "<div>abc</div><p><em><i>test test test</b></em></p>"


# In[60]:


re.split("[<>]",test)


# In[95]:


matrix = ["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14, 15]"]
numbers = [] 
for i in range(len(matrix)):
    temp = re.split("[\[,\]]",matrix[i])
    temp_num = []
    for letter in temp:
        letter = letter.strip()
        if letter.isdigit():
            temp_num.append(int(letter))
    print(temp, temp_num)
    numbers.append(temp_num)
            
    


# In[97]:


numbers


# In[109]:


# 틀린 풀이
row = len(numbers)
col = len(numbers[0])
start = (0,0)
cnt = 0
while cnt < row*col:
    r,c = start[0], start[1]
    target = numbers[r][c]
    flag = False
    if not(0<= r-1 and c+1 < col) and not(r+1 < row and 0 <= c-1):
        flag = True
    print(target,r,c,flag)

    if flag:
        if r == 0:
            if c < col-1:
                c += 1
            else:
                r += 1
        elif c == 0:
            if r < row -1:
                r += 1
            else:
                c += 1
        flag = False
    else:
        
        if 0<= r+1 < row and 0<= c-1 < col and (r+1,c-1) not in visited:
            r += 1
            c -= 1
        else:
            r -= 1
            c += 1
            
    start = (r,c)
        
    
    
    cnt += 1


# In[153]:


from collections import deque
def BE2ndDiagonal(strArr):
    matrix = strArr
    numbers = [] 
    for i in range(len(matrix)):
        temp = re.split("[\[,\]]",matrix[i])
        temp_num = []
        for letter in temp:
            letter = letter.strip()
            if letter.isdigit():
                temp_num.append(int(letter))
        numbers.append(temp_num)

    start = (0,0)
    row, col = len(numbers), len(numbers[0])
    visited = set()
    path = []
    q = deque([start])
    dx = [+1,-1]
    dy = [-1,+1]
    
    while q:
        r,c = q.popleft()
        if r < 0 or r >= row or c < 0 or c >= col:
            continue
        path.append(numbers[r][c])
        visited.add((r,c))
        flag = False
        for i in range(2):
            tx = r + dx[i]
            ty = c + dy[i]
            if 0 <= tx < row and 0 <= ty < col:
                if (tx,ty) not in visited:
                    q.append((tx,ty))
                    flag = True
        if not flag:
            if r == 0 and c < col-1:
                q.append((r,c+1))
            elif c+1 == col:
                q.append((r+1,c))
            elif c == 0 and r < row-1:
                q.append((r+1,c))
            elif r+1 == row:
                q.append((r,c+1))
            flag = False
    return path


# In[154]:


m = ["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14, 15]"]
m = ["[1,2,3]","[4,5,6]","[7,8,9]"]
BE2ndDiagonal(m)


# In[155]:


for i in range(len(numbers)):
    print(numbers[i])


# In[ ]:




