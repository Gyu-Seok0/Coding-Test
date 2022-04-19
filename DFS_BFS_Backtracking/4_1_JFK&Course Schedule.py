#https://leetcode.com/problems/reconstruct-itinerary/
#풀이1
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list) #list형태로 dict저장가능
        for a, b in sorted(tickets):
            graph[a].append(b)

        def dfs(city):
            while graph[city]:
                dfs(graph[city].pop(0)) #city에 있는 앞에 부분을 계속해서 탐색
            route.append(city) #맨마지막 목적지부터 차근차근 넣음

        route = []
        dfs("JFK")
        return route[::-1] # 마지막에 뒤집어줌.

#풀이2
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        def dfs(city):
            while graph[city]:
                dfs(graph[city].pop())
            route.append(city)

        route = []
        dfs("JFK")
        return route[::-1]

# stack으로 문제해결
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)

        route = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop()) # 이 부분이 막힌걸 뚫어주는 코드임.

        return route[::-1]

# 207. Course Schedule
# 선수과목과 후수과목의 관계가 제대로 있는 경우는 True, 아닌 경우는 False가 주어진다.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(node, check):
            if check[node]:  # 이미 해당 노드가 체크되어 있다는 것은 Cycle이 존재한다는 얘기임
                return False
            if len(graph[node]) == 0:  # leaf에 다다름을 의미하므로 back
                return
            check[node] = True  # node를 체크함
            while graph[node]:
                if dfs(graph[node].pop(), check[:]) == False:  # 만약 False라면 더이상 돌릴 필요 없이 False를 리턴한다.
                    return False

        # 1 graph -> Graph를 저장하면서, 초기 시작점을 찾기위해 init부분을 저장한다.
        graph = [[] for _ in range(numCourses)]
        init = [False] * numCourses
        for after, before in prerequisites:
            graph[before].append(after)
            init[after] = True

        # 2 init nodes -> 초기 시작점을 찾는다. 이때 before중에서 가장 root인 것들로 모으면 된다.
        init_nodes = []
        for idx, node in enumerate(init):
            if not node:
                init_nodes.append(idx)

        if len(init_nodes) == 0:  # 초기 시작점이 없다는 말은 False를 리턴해주자.
            return False

        # 3 dfs
        check = [False] * numCourses
        for node in init_nodes:  # 초기 시작점부터 시작해서 dfs를 돌린다.
            if dfs(node, check[:]) == False:  # False를 받으면 더이상 돌릴 필요 없다.
                return False

        # 4 final_check -> 다 돌렸는데도 그래프에 남은 지점이 있다는 것은 가지 못했다는 것을 의미한다. 이는 False를 의미한다.
        for i in range(len(graph)):
            if len(graph[i]) > 0:
                return False

        return True  # 맨마지막에 True를 리턴해준다.

# 풀이2 -> time exceed
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)  # sibling들도 이 값에 접근할 수 있으므로.. 삭제해준다.
            return True

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 방문 노드를 저장
        traced = set()
        for x in list(graph):
            if not dfs(x):
                return False
        return True

# solution3 -> visited 추가 -> 무려 10배나 더 빨라짐.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            # 순환구조
            if i in traced:
                return False
            # 이미 방문
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)  # sibling들도 이 값에 접근할 수 있으므로.. 삭제해준다.
            visited.add(i)
            return True

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 방문 노드를 저장
        traced = set()
        visited = set()
        print(graph, list(graph))
        for x in list(graph):
            if not dfs(x):
                return False
        return True



