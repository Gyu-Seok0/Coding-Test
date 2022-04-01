#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 브루트포스 -> 시간초과
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 오른쪽에서 가장 max인 값과 자기자신의 차이 max인 값을 찾으면 될듯 싶다.
        profit = 0
        for idx in range(len(prices) - 1):
            profit = max(max(prices[idx + 1:]) - prices[idx], profit)
        return profit

# 투포인터 -> 틀림 (left, right을 같이 움직이면 안됌)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 투포인터를 이용하자 (왼쪽에서는 가장 작은 값을 찾고, 오른쪽에서는 가장 큰 값을 찾아서 두 개를 빼주면 된다.

        left, right = 0, len(prices) - 1
        buy, sell = 1e4, 0
        while right >= left:
            buy = min(buy, prices[left])
            sell = max(sell, prices[right])
            left += 1
            right -= 1

        return max(0, sell - buy)

# 최소값과 최대값을 계속 업데이트.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(price,min_price) # 이전 값으로 min_price 업데이트
            profit = max(profit, price - min_price) # 최대 값은 for문을 돌면서 업데이트
        return profit


#https://leetcode.com/problems/palindrome-linked-list/submissions/
# 내풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = [head.val]
        after = head.next
        while after:
            values.append(after.val)
            after = after.next
        return values == values[::-1]

#
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q:List = [head.val]
        after = head.next
        while after:
            q.append(after.val)
            after = after.next
        while len(q) > 1:
            if q.pop(0) != q.pop(): # 동적 배열로 구성된 리스트에서 앞부터 꺼내오면서 문제가 발생한다 -> 인덱스가 모두 한칸씩 앞으로 움직이는 쉬프팅이 발생하므로, O(n)시간 복잡도가 소요된다.
                return False
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()

        if not head:
            return False

        node = head
        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 런너 기법.. 미쳤다
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next  # fast가 존재한다면 홀수이고, fast가 None이 된다면 짝수개임
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev