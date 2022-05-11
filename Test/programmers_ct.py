#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(atmos):
    state = 1
    mask,day,cnt = False, 0, 0
    for a,b in atmos:
        if a >= 151 and b >= 76:
            state = 3
        elif 81 <= a <= 150 or 36 <= b <= 75:
            state = 2
        else:
            state = 1
        
        if state == 1 and mask:
            day += 1
        elif state == 2:
            if mask:
                day += 1
            else:
                mask, day = True, 1
        elif state == 3:
            if mask:
                day = 3
            else:
                mask, day = True,3

        if day >= 3:
            mask,day = False, 0
            cnt += 1
            
    if mask:
        cnt += 1
    return cnt


# In[ ]:


def solution(atmos):
    answer = -1
    mask, day = False, 0
    cnt = 0
    for a,b in atmos:
        if a >= 151 and b >= 76:
            state = 3
        elif a >= 81 or b >= 36:
            state = 2
        else:
            state = 1

        if mask:
            if state == 1 or state == 2:
                day += 1
            elif state == 3:
                day += 3
        else:
            if state == 2:
                mask, day = True, 1
            elif state == 3:
                mask, day = True, 3
        
        if day >= 3:
            cnt += 1
            mask, day = False, 0
            
    if mask:
        cnt += 1
    return cnt


# In[ ]:


from collections import defaultdict

def solution(rooms, target):
    answer = []

    people = defaultdict(list)
    room = defaultdict(list)

    for r in rooms:
        num, they =  r.split(']')
        num = num[1:]
        they = they.split(',')

        room[num] += they
        for person in they:
            people[person] += [num]

    candidate = []
    for person, bangs in list(people.items()):
        if str(target) in bangs:
            continue
        distance = 1e9
        for bang in bangs:
            distance = min(distance, abs(int(bang) - int(target)))
        candidate.append((len(bangs),distance,person))
    
    result = sorted(candidate, key = lambda x: (x[0],x[1],x[2]))
    return [r[2] for r in result]


# In[51]:


"Q4OYPI".split()


# In[ ]:


def solution(line):
    def cal(p1,p2):
        y = abs(p1[0] - p2[0])
        x = abs(p1[1] - p2[1])
        return x+y, x

    key = {'1': (1,1), '2':(1,2), '3': (1,3), '4':(1,4), '5': (1,5), '6':(1,6), '7': (1,7), '8':(1,8), '9':(1,9), '0':(1,10),
            'Q': (2,1), 'W':(2,2), 'E':(2,3), 'R':(2,4), 'T': (2,5), 'Y': (2,6), 'U':(2,7), 'I':(2,8), 'O':(2,9), 'P':(2,10)}
    hand = {'left':['1','2','3','4','5','Q','W','E','R','T']}

    left, right = key['Q'], key['P']
    answer = []
    flag = 1
    for letter in line:
        l_m, l_h = cal(left,key[letter])
        r_m, r_h = cal(right,key[letter])
 
        if l_m < r_m:
            left = key[letter]
            answer.append(0)
    
        elif r_m < l_m:
            right = key[letter]
            answer.append(1) 
        else:
            if l_h < r_h:
                left = key[letter]
                answer.append(0)
            elif r_h < l_h:
                right = key[letter]
                answer.append(1)
            else:
                if letter in hand["left"]:
                    left = key[letter]
                    answer.append(0)
                else:
                    right = key[letter]
                    answer.append(1)

    return answer

