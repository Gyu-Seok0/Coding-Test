#https://leetcode.com/problems/reverse-linked-list/submissions/
# 역순으로 링크드 리스트를 만드는 문제인데, 어렵진 않았지만 재귀로 푸는 걸 이해하는 게 살짝 시간이 걸렸다.

# 내 풀이(반복문)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev


# 재귀풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev # 이전값 기록
            return reverse(next,node)
        return reverse(head)