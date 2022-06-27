# https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
backpropagation을 이용해서 계속해서 leaf node에서 천천히 올라오면 되는데.. ㅠㅠ
이때 상태값으로 max(left,right)를 주는 이유는 바로 layer의 깊이라고 생각하면 되겠다.

'''

class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left + right)
            return max(left, right)

        dfs(root)
        return self.longest

# 틀린코드1
#         def dfs(root):
#             if not root:
#                 return -1

#             left = dfs(root.left)
#             right = dfs(root.right)

#             if root.left and root.right:
#                 if root.left.val == root.right.val == root.val:
#                     self.longest = max(self.longest, left + right + 2)
#                     return left + right + 1
#                 else:
#                     if root.left.val == root.val:
#                         self.longest = max(self.longest, right)
#                         return left + 1

#                     elif root.right.val == root.val:
#                         self.longest = max(self.longest, left)
#                         return right + 1

#             if root.left:
#                 if root.left.val == root.val:
#                     return left + 1
#                 else:
#                     self.longest = max(self.longest, left)
#                     return 0
#             if root.right:
#                 if root.right.val == root.val:
#                     return right + 1
#                 else:
#                     self.longest = max(self.longest, right)
#                     return 0
#         dfs(root)
#         return self.longest

# 틀린코드2
#         def dfs(root, length):
#             # Base
#             if not root:
#                 return -1

#             if not root.left and not root.right:
#                 self.longest = max(self.longest, length)
#                 return

#             # recursive
#             if root.left:
#                 if root.left.val == root.val:
#                     dfs(root.left, length + 1)
#                 else:
#                     self.longest = max(self.longest, length)
#                     dfs(root.left, 0)
#             if root.right:
#                 if root.right.val == root.val:
#                     dfs(root.right, length + 1)
#                 else:
#                     self.longest = max(self.longest, length)
#                     dfs(root.right, 0)
#             if root.left and root.right:
#                 if root.left.val == root.right.val == root.val:
#                     dfs(root.left, length + 2)
#                     dfs(root.right, length + 2)

#         dfs(root,0)
#         return self.longest