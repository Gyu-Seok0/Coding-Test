#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2번
from collections import deque
def solution(queue1, queue2):
    q1,q2 = deque(queue1), deque(queue2)
    target, rest = divmod(sum(q1) + sum(q2), 2)
    # 홀수인경우 제외
    if rest != 0:
        return -1
    
    cnt = 0
    while q1 and q2:
        if sum(q1) == sum(q2) == target:
            return cnt
        if sum(q1) > target:
            num = q1.popleft()
            q2.append(num)
        elif sum(q2) > target:
            num = q2.popleft()
            q1.append(num)
        cnt += 1
    return -1


# In[84]:


# 4번?
from collections import deque
import copy
def solution(n, paths, gates, summits):
    answer = []
    graph = [[0]*(n+1) for _ in range(n+1)]
    for a,b,c in paths:
        graph[a][b] = graph[b][a] = c
    print(graph)
    
    def dfs(start,end,intensity,visit,other):
        print(start,end,intensity,visit)
        if start == end:
            print("answer", start,end,intensity,visit)

            result.append((end,intensity))
            return
        visit[start] = True
        for node in range(n+1):
            if not visit[node] and graph[start][node] != 0 and node not in gates and node not in other:
                dfs(node,end,max(intensity,graph[start][node]),visit[:],other)

    result = []
    for start in gates:
        for end in summits:
            other = copy.deepcopy(summits)
            other.remove(end)
            visited = [False]*(n+1)
            visited[start] = True
            for node in range(n+1):
                if not visited[node] and graph[start][node] != 0 and node not in gates and node not in other:
                    print("start",start)
                    dfs(node,end,graph[start][node],visited[:],other)
        
    answer = sorted(result, key = lambda x: (x[1],x[0]))[0]
    print(answer)
    return answer


# In[ ]:


# 5번
from copy import deepcopy

def solution(rc, operations):
    def ShiftRow(board):
        return [board[-1]]+ board[:-1]
    
    def Rotate(board):
        t = list(zip(*board))

        row1 = board[0][:-1]
        col1 = list(t[-1][:-1])
        row2 = board[-1][1:]
        col2 = list(t[0][1:])

        new_board = deepcopy(board)
        new_board[0][1:] = row1
        new_board[-1][:-1] = row2

        temp = list(zip(*new_board))
        temp[-1] = [temp[-1][0]] + col1
        temp[0] = col2 + [temp[0][-1]]
        return list(map(list,zip(*temp)))

    for op in operations:
        if op == "Rotate":
            rc = Rotate(rc)
        else:
            rc = ShiftRow(rc)
    return rc


# In[ ]:




