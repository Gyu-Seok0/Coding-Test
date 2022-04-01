# https://leetcode.com/problems/number-of-islands/submissions/
'''
섬을 찾는 문제였다.
여기서 섬이란 가로,세로로 "1"로 이어지는 영역을 의미한다.
풀이 방식은 가로축과 세로축으로 DFS를 활용하였다.
'''
class Solution:
    def search(self, x: int, y: int, grid, candidate):
        dx = [1, -1, 0, 0]  # right, left, down, up
        dy = [0, 0, -1, 1]
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < len(grid) and 0 <= ty < len(grid[tx]) and grid[tx][ty] == "1":
                candidate.remove((tx, ty))
                grid[tx][ty] = "0"
                self.search(tx, ty, grid, candidate)

    def numIslands(self, grid: List[List[str]]) -> int:
        # x,y를 받기.
        candidate = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    candidate.append((row, col)) # 굳이 이렇게 후보군을 모을 필요가 없었던 코드였다.
        island = 0
        while candidate:
            x, y = candidate.popleft()
            grid[x][y] = "0"
            island += 1
            self.search(x, y, grid, candidate)
        return island


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):  # 부모함수의 parameter를 같이 참조한다.
            # Base
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1":
                return
            # Iterative
            grid[x][y] = "0"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        # x,y를 받기.
        island = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    island += 1

        return island
'''
개선한 점
1) 파라미터를 계속 넘겨주지 않기 위해서, Nested Function을 사용하였다.
2) 후보군을 모으지 않고, 후보를 만나는 즉시 dfs를 수행하였다
3) DFS를 4번 호출하였다.
4) DFS 조건문 조건으로 or문을 사용하였다.
'''

#https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(rest_numbers):
            if not rest_numbers:
                return [""]
            target = rest_numbers.popleft()
            child = backtrack(rest_numbers)
            parent = []
            for value1 in d[target]:
                for value2 in child:
                    parent.append(value1 + value2)
            return parent

        if not len(digits):
            return []

        numbers = deque([digit for digit in digits])
        d = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}

        return backtrack(numbers)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):  # 0 ~3 -> 1 ~ 3 -> 2 ~ 3
                for letter in d[digits[i]]:
                    dfs(i + 1, path + letter)

        if not digits:
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(index, combination):
            if index == len(digits):
                return combination
            for candidate in d[digits[index]]:
                ans = backtracking(index + 1, combination + candidate)
                if ans:
                    result.append(ans)

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        backtracking(0, "")
        return result