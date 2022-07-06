# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 내가 짠 코드
class Solution:
    def __init__(self):
        self.answer = True

    def isBalanced(self, root: Optional[TreeNode]):
        def dfs(root):
            # dfs로 가장 밑까지

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if not self.answer:
                return

            if abs(left - right) > 1:
                self.answer = False
                return

            return max(left, right) + 1

        dfs(root)
        return self.answer


# 정답코드
class Solution:
    def isBalanced(self, root: Optional[TreeNode]):
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left,right) + 1
        return check(root) != -1

-> 뭔가 False나 -1과 같은 상황이 발생했을때, 호출한 모든 재귀를 다 없애는 방식을 취하고 싶은데 방법이 없나?