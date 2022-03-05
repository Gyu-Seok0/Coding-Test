from typing import List
# leetcode1: sum of two numbers
class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums:
                return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

s1 = solution()
print(f"s1's answer = {s1.twoSum([2,7,11,15], 9)}")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i,num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

'''
* list의 Method인 index를 활용하는 방식
* Dict에서 indexing하는 것은 해쉬테이블을 이용하기 때문에 O(1)이 걸려서 훨씬 빠른 풀이를 가져다 준다.
'''


# https://leetcode.com/problems/trapping-rain-water/
# 투포인터를 사용해서, left와 right가 최대지점에서 만나도록 하는 것

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while right > left:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):

            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:  # 현재
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        print(stack)
        return volume


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            # 변곡점을 만난다면,
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                x = i - stack[-1] - 1
                y = min(height[i], height[stack[-1]]) - height[top]
                volume += x * y

            stack.append(i)
        return volume