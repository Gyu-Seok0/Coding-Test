#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
'''
정렬된 두개의 Linked List를 하나의 정렬된 Linked List로 만드는 문제였다.
Linked List가 단방향으로 연결되다보니, 가장 최초의 node에 값을 추가하여 연결 리스트를 만드는 것에 문제가 있었으나
첫번째 node를 버리는 값으로 생각하고 문제를 해결할 수 있었다.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        head = answer

        head1, head2 = list1, list2
        while head1 and head2:
            if head1.val < head2.val:
                head.next = ListNode(head1.val)
                head, head1 = head.next, head1.next
            else:
                head.next = ListNode(head2.val)
                head, head2 = head.next, head2.next

        while head1:
            head.next = ListNode(head1.val)
            head, head1 = head.next, head1.next
        while head2:
            head.next = ListNode(head2.val)
            head, head2 = head.next, head2.next

        answer = answer.next  # 맨앞의 값에는 아무것도 존재하지 않으므로, next시킨다.
        return answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
'''
l1.next가 None이 되고나서 -> mergeTwoLists -> swap을 하면 l2가 none이 됌
이후 l1은 뭔가가 존재하고, l2는 None이 되니까 첫번째 if문은 생략하고, 두번째 if문을 계속해서 돌게된다.
결국 l1.next가 None에 다다르면, return을 시작하는 백트리킹 방식이다 -> 대박
'''