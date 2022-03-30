# https://leetcode.com/problems/combination-sum/submissions/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(temp, need):
            if sum(temp) == target:
                temp.sort()
                if temp not in results:
                    results.append(temp[:])
                return
            elif need < 0:
                return
            else:
                for num in candidates:
                    if need >= num:
                        temp.append(num)
                        dfs(copy.deepcopy(temp), need - num)
                        temp.pop()
                return
                        
        results = []
        dfs([],target)
        return results

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                results.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i],i, path + [candidates[i]])
        results = []
        dfs(target, 0, [])
        return results


'''
조합의 합에서 효율성을 높일 수 있는 방법은 자기자신부터 하위원소까지의 나열로만 정리하는 것이었다.
두번째 solution을 보게되면, for문의 범위가 자기자신 ~ 하위원소까지로 한정되어있었다.
이를 통해 첫번째 풀이보다 10배나 더 빠른 풀이가 가능했다.
'''