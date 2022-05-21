from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph 저장
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(i):
            if i in visited:
                return True
            if i in traced:
                return False

            traced.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        visited = set()  # 이미 완벽히 Search한 node들에 대해서는 굳이 돌 필요가 없음.
        traced = set()  # Cycle이 존재한다면, 결과적으로 서로를 가르키고 있는 것이므로 문제가 됌.

        for i in list(graph):
            if not dfs(i):
                return False
        return True



