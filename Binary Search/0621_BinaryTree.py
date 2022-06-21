# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(1,root)])
        ans = 1
        while q:
            layer, node = q.popleft()
            ans = max(layer,ans)
            if node.left:
                q.append((layer+1, node.left))
            if node.right:
                q.append((layer+1, node.right))
        return ans

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)): # L번쨰 layer들의 모든 Node들이 담김
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth

'''
첫번째 풀이가 내 풀이이고, 두번째 풀이가 책에 적힌 풀이이다. 
시간대는 내가 더 빠르게 풀이가 되었다. 그러나 특정 layer의 모든 node들을 for문에서 모두 popleft시키고 child node들을 다시 q에 채워나가는 방식에서 흥미롭다고 생각했다.
더불어서, if not root와 같은 형태로 exception을 잡아주는 노력을 시도했어야 했다.
'''

#https://leetcode.com/problems/diameter-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def __init__(self):
        self.longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2) # 거리
            return max(left, right) + 1 #상태값

        dfs(root)
        return self.longest

'''
위 문제는 dfs를 이용해서 leaf node까지 도달한 다음, 거리와 상태값을 업데이트 한다.
이때 거리는 left와 right에 +2 (한 node를 기준으로 left에 대한 edge 1개 + right에 대한 edge가 1개) 이기 때문이다.
그리고 상태값은 해당 Node가 가질 수 있는 최대 깊이(?)라고 생각이 가능하다. 
이때 하나의 전역변수인 self.longest를 이용해서 binary tree에 존재하는 모든 거리에 대해서 max로 비교하였다.

아직까지 코딩이 너무 부족하다고 많이 느낀다 ㅠㅠ
'''