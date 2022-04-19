class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(target,idx, cnt):
            results.append(target)
            if cnt <= 0: # 어차피 idx가 len(nums)를 넘으면 필요없는 조건이 되는구나.
                return
            for i in range(idx+1,len(nums)):
                dfs(target + [nums[i]], i, cnt-1)
                
        results = []
        dfs([],-1,len(nums))
        return results

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index,path):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
        result = []
        dfs(0,[])
        return result