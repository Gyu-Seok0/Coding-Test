# https://www.acmicpc.net/problem/1916

import sys

node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())


# 다익스트라
import heapq

INF = int(1e9)
distance = [INF] * (node + 1)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    cost, node = heapq.heappop(q)
    if distance[node] < cost:
        continue

    for new, new_cost in graph[node]:
        print(new, new_cost)
        if distance[new] > distance[node] + new_cost:
            distance[new] = distance[node] + new_cost
            heapq.heappush(q, (distance[new], new))

print(distance[end])