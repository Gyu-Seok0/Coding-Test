class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        #누적해서 가져가기
        def dfs(start, temp):
            if len(temp) == k:
                result.append(temp)
                
            for num in range(start+1,n+1):
                dfs(num, temp + [num]) #이렇게 더해서 주면, 새로운 객체를 참조한다.
                
        result = []
        dfs(0,[])
        return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def dfs(elements,start:int, k:int):
            if k == 0:
                results.append(elements[:])
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements,i+1, k-1)
                elements.pop()
        dfs([],1,k)
        return results

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1), k))
