class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(cnt, temp):
            if cnt == len(nums):
                answer.append(temp[:]) #파이썬이 객체여서 temp값 하나의 주소값에 모든 값들이 다 바뀌는 형태임..
                return
            
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs(cnt+1, temp)
                    temp.pop()
        
        answer = []
        dfs(0,[])
        return answer

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0: #마지막 노드에 다다르면,
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


'''
파이썬은 모든 것이 객체로 된 언어이다.
예를 들어 a = [1,2,3]이 있고
b = a
b.append(4)
print(a) -> [1,2,3,4]가 된다.

첫번째 함수에서 변수를 temp로 지정해서 DFS를 수행하는데, 수행하면서 temp값이 계속바뀌게 되고 종국에는
가장 마지막에 적용된 temp로 모두 저장되는 불상사가 발생한다.
이를 막기 위해서는 temp[:] 혹은 copy.deepcopy와 같이 새로운 객체를 선언하면 된다. 

'''