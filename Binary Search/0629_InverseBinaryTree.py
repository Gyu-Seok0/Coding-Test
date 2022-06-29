https://leetcode.com/problems/invert-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 밑바닥까지 가서 좌우를 바꿔주면 됌.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# DFS 풀이(stack이용)
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left

        return root

# BFS 풀이 (queue 이용)
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

# 가장 간단한 풀이
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 내풀이
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)
            node.left, node.right = right,left
            return node
        dfs(root)
        return root