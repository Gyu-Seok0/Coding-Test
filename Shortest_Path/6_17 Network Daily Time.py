#https://leetcode.com/problems/network-delay-time/
# 내 풀이
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # heapq
        q = []
        heapq.heappush(q, (0, k))

        # graph
        graph = [[1e9] * (n + 1) for _ in range(n + 1)]
        for a, b, c in times:
            graph[a][b] = c

        # distances
        distances = [1e9] * (n + 1)
        distances[0] = 0
        distances[k] = 0

        # 원래거리랑 시작점 + edge를 비교해서 작은 걸 주면될듯?

        while q:
            cost, node = heapq.heappop(q)
            if distances[node] < cost:
                continue

            for new, new_cost in enumerate(graph[node]):
                if distances[new] > distances[node] + new_cost:
                    distances[new] = distances[node] + new_cost
                    heapq.heappush(q, (distances[new], new))
        ans = max(distances)
        return ans if ans != 1e9 else -1

# 정답풀이
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        dist = defaultdict(int)
        for a,b,c in times:
            g[a].append((b,c))
        q = []
        heapq.heappush(q,(0,k))
        while q:
            cost, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = cost
                for v,w in g[node]:
                    alt = cost + w
                    heapq.heappush(q,(alt,v))
        return max(dist.values()) if len(dist) == n else -1

# https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/
# https://8iggy.tistory.com/115

import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        visit = {} # 거쳐간 도시의 개수
        Q = [(0, src, 0)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] >= k:  # 아직방문을 안했거나, 해당노드를 방문하기 전에 경유지가 더 적어야한다.
                visit[node] = k
                if k <= K:
                    for v, w in graph[node]:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1

'''
Line70에 대해서 부가설명을 하자면, 기본적으로 price-node-k는 우선순위 큐로부터 나왔기 때문에,
visit[node]는 최단거리일때 거쳐간 도시의 개수가 된다. 따라서 이보다 더 최단거리가 나오려면,
기본적으로 visit[node]보다 더 많은 방문횟수가 요구될 것이다. (근데 내 생각에는 visit[node] >= k, 라고해도 무방할 것 같아서 그렇게 풀이를 했고 오히려 run-time시간이 훨씬 줄었다)
'''