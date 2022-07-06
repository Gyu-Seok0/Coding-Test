#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None

        nums = deque(data.split())
        root = TreeNode(int(nums.popleft()))
        q = deque([root])

        while q:
            node = q.popleft()
            num = nums.popleft()
            if num != "#":
                node.left = TreeNode(int(num))
                q.append(node.left)
            num = nums.popleft()
            if num != "#":
                node.right = TreeNode(int(num))
                q.append(node.right)
        return root


''' 이 문제를 못푼 이유
1) 역직렬화 과정에서 너무 어렵게 생각함. 
Binary Tree에서 왼쪽 child는 *2, 오른쪽 child는 *3 이런 식인데, 이렇게 짜면 코드가 굉장히 복잡해짐.

2) 역직렬화 과정에서 while문으로 해당 node의 값 하나만 처리하는 과정에서 문제발생
node.left = TreeNode()로 그냥 queue에 넣으니까, 나중에 이값을 None으로 바꾸려고 하는 과정에서 문제가 발생함.
이유는 알 수 없지만 node = TreeNode()로 assign하고 나중에 None로 assign이 제대로 안되는 것 같음.
-> while문 안에서
 1. left, right 값 모두 처리
 
 2. 애초에 "#"으로 나오면 left든 right든 아무런 assign을 하면 안됌. 

그래서 뭔가 이 문제는 좀 할당하는 과정에서 문제가 있는 것으로 보임.
'''

