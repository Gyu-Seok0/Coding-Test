#https://leetcode.com/problems/array-partition-i/submissions/
# 배열 분할


from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i in range(0,len(nums),2):
            answer += nums[i]
        return answer

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                mul *= num

        answer = []
        for idx, num in enumerate(nums):
            if zero_cnt > 1 or (zero_cnt > 0 and num != 0):
                answer.append(0)
            elif zero_cnt == 1 and num == 0:
                answer.append(mul)
            else:
                answer.append(mul // num)
        return answer

class solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        p = 1
        for i in range(len(nums)):
            out[i] *= p
            p *= nums[i]
        p = 1
        for j in range(len(nums)-1,-1,-1):
            out[j] *= p
            p *= nums[j]
        return out
