# 와셜플로이드
# https://www.acmicpc.net/problem/1389

user, friend = map(int, input().split())
graph = []
for i in range(user + 1):
    graph.append([1e9] * (user + 1))
    graph[i][i] = 0

for _ in range(friend):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, user + 1): # k가 여기에 들어와야 알고리즘이 수행된다.
    for a in range(1, user + 1):
        for b in range(1, user + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result, min_value = 1, 1e9
for node in range(1, user + 1):
    node_sum = 0
    for distance in graph[node]:
        if distance != 1e9:
            node_sum += distance
    if min_value > node_sum:
        result, min_value = node, node_sum
print(result)