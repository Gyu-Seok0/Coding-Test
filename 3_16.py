#https://leetcode.com/problems/add-two-numbers/
# 주어진 링크드리스트를 거꾸로 반환해서 더한후, 다시 거꾸로 반환하면 되는 문제였다.
# 사실 거꾸로가 두번이여서 헷갈리는 부분이 있었지만, 주어진 숫자를 앞에서부터 읽어 나가면 된다.
# 예를 들어 123이라는 숫자가 주어지면 일의자리=1, 십의자리=2, 백의자리=3 이런 식으로 수행하면 된다.
# 구체적인 예시는 아래와 같다.
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

#풀이1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check_over_ten(self, num):
        if num >= 10:
            return num - 10, 1
        else:
            return num, 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans

        add, flag = 0, 0
        while l1 or l2:
            if not l1:
                add, flag = self.check_over_ten(l2.val + flag)
                l2 = l2.next

            elif not l2:
                add, flag = self.check_over_ten(l1.val + flag)
                l1 = l1.next

            else:
                add, flag = self.check_over_ten(l1.val + l2.val + flag)
                l1, l2 = l1.next, l2.next

            head.next = ListNode(add)
            head = head.next

        if flag:
            head.next = ListNode(flag)

        return ans.next


#풀이2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next

            if l2:
                add += l2.val
                l2 = l2.next

            carry, add = divmod(add + carry, 10)
            head.next = ListNode(add)
            head = head.next

        return root.next


'''
느낀점
1) 변수이름: carry, root와 같은 부분 이해하기
2) divmod: 몫, 나머지를 반환하는 함수
'''


# 주어진 리스트를 하나의 숫자로 표현하는 방법
import functools

# 누적해서 더하기
a = [1,2,3,4,5]
ans = int(''.join(str(e) for e in a))
print("for",ans)

ans = int("".join(map(str,a)))
print("map", ans)

ans = functools.reduce(lambda x,y:10*x+y,[1,2,3,4,5],0) # 누적해서 더해지는 개념이라고 생각하면 된다. 이때 0은 (0)12345 으로 맨 앞자리에 숫자가 되는 것 같다.
print("Reduce",ans)

# 링크드 리스트를 거꾸로 뒤집는 방법
def reverseList(self, head: ListNode):
    node, prev = head, None

    while node:
        # 방법1
        next, node.next = node.next, prev
        node, prev = next, node

        # 방법2
        # prev, prev.next, node = node, prev, node.next
    return prev


# List를 링크드리스트로 연결하는 방법
def toList(self, node: List) -> List:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list


# 리스트를 연결리스트로 반대로 변경하는 함수
def toReversedLinkedList(self, result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)  # node는 계속 새롭게 assign
        node.next = prev
        prev = node

    return node  # prev해도 됌

