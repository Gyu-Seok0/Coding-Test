# 내풀이
def solution(numbers, target):
    global answer
    answer = 0

    def dfs(total, numbers):
        global answer
        if len(numbers) == 0:
            if total == target:
                answer += 1
            return
        num = numbers[0]
        dfs(total + num, numbers[1:])
        dfs(total - num, numbers[1:])

    dfs(0, numbers)
    return answer

# 다른풀이 (깔끔 그 자체)
# 재귀를 정말 잘 이해한다면 (binary search형태로 마지막 leaf들부터 summation 형태로 root까지 도달한다느 점을 이해할 수 있을 것이다.
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    if not numbers:
        return 0
    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])