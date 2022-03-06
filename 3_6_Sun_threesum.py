# https://leetcode.com/problems/3sum/
# 브루트포스 -> O(N3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        check = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i == j or j== k or k == i:
                        continue
                    else:
                        if nums[i] + nums[j] + nums[k] == 0 and {i,j,k} not in check:
                            answer.append(sorted([nums[i], nums[j], nums[k]]))
                            check.append({i,j,k})
        return list(set([tuple(item) for item in answer]))

# 투포인터 사용하는방법 -> O(N2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복방지
                continue
            left, right = i + 1, len(nums) - 1

            while right > left:
                target = [nums[i], nums[left], nums[right]]
                sum_target = sum(target)
                if sum_target == 0:
                    answer.append(target)
                    while left > right and nums[left] == nums[left + 1]:  # 중복방지
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 중복방지
                        right -= 1
                    left += 1
                    right -= 1
                elif sum(target) > 0:
                    right -= 1
                else:
                    left += 1
        return answer