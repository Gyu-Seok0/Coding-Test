# 동빈's
def balance(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i


def check_proper(p):  # 굳이 스택을 안쓰는 구나.
    cnt = 0
    for letter in p:
        if letter == '(':
            cnt += 1
        else:
            if cnt == 0:  # 균형잡히지 않음.("("4번이랑, ")"5번하면.. cnt = 0이 됌) -> 근데 조건을 너무 어렵게 표현한것일 수도 있음,.
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balance(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # u가 적합하다면,
    if check_proper(u):
        answer = u + solution(v)  # 재귀를 여기서 돌리는 구나
    # u가 적합하지 않다면,
    else:
        answer = '(' + solution(v) + ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

# 이렇게 풀이가능(정답)
def solution(p):
    # 종료조건
    if p == '':
        return ''
    cnt, correct = 0, True
    for idx in range(len(p)):
        if p[idx] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0: #올바른 문자열인가(?)
            correct = False
        if cnt == 0: #균형잡힌 문자열인가(?)
            if correct:
                return p[:idx+1] + solution(p[idx+1:])
            else:
                return "(" + solution(p[idx+1:])+")" + "".join(list(map(lambda x: "(" if x == ")" else ")", p[1:idx])))
