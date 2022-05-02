def solution(n, s, a, b, fares):
    INF = 1e9
    graph = []
    # 초깃값
    for i in range(n + 1):
        graph.append([INF] * (n + 1))
        graph[i][i] = 0

    # graph 불러오기
    for start, end, cost in fares:
        graph[start][end] = graph[end][start] = cost

    inter = -1
    for k in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
    # 우와 이것도 점화식이구나.. 수학은 대단해
    answer = INF
    for t in range(1, n + 1):
        answer = min(answer, graph[s][t] + graph[t][a] + graph[t][b])
    return answer