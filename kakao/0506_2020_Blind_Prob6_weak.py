# 내풀이
from copy import deepcopy
def solution(n, weak, dist):
    global answer
    g = [0] * n
    for w in weak:
        g[w] = 1

    def dfs(g, dist, cnt):
        global answer
        if cnt >= answer > 0:
            return

        if 1 not in g:
            if answer <= 0:
                answer = cnt
            else:
                answer = min(answer, cnt)
            return

        elif len(dist) == 0:
            return  # 이미 answer = -1로 지정해놓음.

        for idx, d in enumerate(dist):
            for i in range(n):
                if g[i] == 1:
                    g[i] = 0
                    g_left, g_right = deepcopy(g), deepcopy(g)
                    l_flag, r_flag = False, False
                    left = right = i
                    target = d
                    while target > 0:
                        left, right = left - 1, right + 1
                        if left == -1:
                            left = n - 1
                        if right == n:
                            right = 0
                        if g_left[left] == 1:
                            g_left[left] = 0
                            l_flag = True
                        if g_right[right] == 1:
                            g_right[right] = 0
                            r_flag = True
                        target -= 1

                    dist.pop(idx)
                    if l_flag:
                        dfs(g_left[:], dist[:], cnt + 1)
                    if r_flag:
                        dfs(g_right[:], dist[:], cnt + 1)
                    dist.insert(idx, d)
                    g[i] = 1

    answer = -1
    dist.sort(reverse=True)
    dfs(g, dist, 0)

    return answer

# 정답
# 나는 시계반대방향을 생각했는데, 이건 아무도 한것 같지는 않다.

from collections import deque
def solution(n, weak, dist):
    dist.sort(reverse = True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)): # 거리
        d = dist[i]
        for _ in range(len(q)): # weak
            current = q.popleft()
            for p in current: # weak point
                l = p
                r = (p+d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: r < x < l, current))
                if len(temp) == 0:
                    return (i+1)
                elif temp not in visited: # 이전에 방문한적이 있다면, 이미 q에 들어가 있을 것이므로 굳이 또 넣을 필요가 없다.
                    visited.add(temp)
                    q.append(list(temp))
    return -1