#https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    for k in range(1, len(s) // 2 + 1):
        target = s[:k]
        string, cnt = "", 1

        for i in range(k, len(s), k):
            if target == s[i:i + k]:
                cnt += 1
            else:
                if cnt > 1:
                    string += str(cnt) + target
                    cnt = 1
                else:
                    string += target
            target = s[i:i + k]
        if cnt > 1:
            string += str(cnt) + target
        else:
            string += target

        answer = min(answer, len(string))

    return answer


def solution(s):
    length = len(s)
    answer = length

    for k in range(1, length // 2 + 1): # for문을 절반만 도는 게 좋다.
        cnt, l_string = 1, length
        for left, right in zip(range(0, length - k, k), range(k, length, k)): # 투포인터로 left, right값을 잡아주었다.
            if s[left:right] == s[right:right + k]:
                cnt += 1
            else:
                if cnt > 1:
                    l_string -= (cnt - 1) * k - len(str(cnt)) # 여기서 cnt값이 두자리수, 세자리수 일수도 있는데 1로 통일하다보니 틀린 정답을 가져왔다.
                    cnt = 1
        if cnt > 1: #맨 마지막에 letter들이 처리가 안됐었을 수도 있어서 여기서 정리해주었다.
            l_string -= (cnt - 1) * k - len(str(cnt))
        answer = min(answer, l_string)
    return answer