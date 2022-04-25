def solution(n, info):
    # 점수를 얻으려면, 무조건 더 많이 쏴야 한다.
    # 화살을 쏘고 -> dfs로 이동 -> 화살이 끝나면, 점수를 계산하면 될듯? -> 내껀 왜 안되는지 (테스트 케이스 두 군데에서 막힘)
    def cal(s):
        me, you = 0, 0
        for i in range(10):
            if info[i] == 0 and s[i] == 0:
                continue
            if info[i] >= s[i]:
                you += 10 - i
            else:
                me += 10 - i
                # print(s, me-you)
        return me - you

    def dfs(cnt, s, idx):
        if cnt <= 0:
            differnce = cal(s)
            if differnce >= answer[1]:
                if len(answer[0]) == 1:
                    answer[0], answer[1] = s, differnce
                    return
                else:
                    for idx in range(10, -1, -1):
                        if s[idx] > answer[0][idx]:
                            answer[0], answer[1] = s, differnce
                            return

        while idx <= 10:
            compare = info[idx] + 1
            if cnt >= compare:
                s[idx] = compare
                dfs(cnt - compare, s[:], idx + 1)
                s[idx] = 0
            if idx == 10:
                s[idx] = cnt
                dfs(0, s[:], idx + 1)
            idx += 1

    answer = [[-1], 1]
    dfs(n, [0] * 11, 0)

    return answer[0]


# 풀이2

import copy

MAX_SCORE_DIFF = 0
answers = []


def calcScoreDiff(info, myshots):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            enemyScore += (10 - i)
        else:
            myScore += (10 - i)
    return myScore - enemyScore


def dfs(info, myshots, n, i):
    global MAX_SCORE_DIFF, answers
    if i == 11:
        if n != 0:
            myshots[10] = n
        scoreDiff = calcScoreDiff(info, myshots)
        if scoreDiff <= 0:
            return
        result = copy.deepcopy(myshots)
        if scoreDiff > MAX_SCORE_DIFF:
            MAX_SCORE_DIFF = scoreDiff
            answers = [result]
            return
        if scoreDiff == MAX_SCORE_DIFF:
            answers.append(result)
        return
    if info[i] < n:
        myshots.append(info[i] + 1)
        dfs(info, myshots, n - info[i] - 1, i + 1)
        myshots.pop()

    myshots.append(0)
    dfs(info, myshots, n, i + 1)
    myshots.pop()


def solution(n, info):
    global MAX_SCORE_DIFF, answers
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key=lambda x: x[::-1], reverse=True)
    return answers[0]

# 풀이3 -> 제일 비효율적인 풀이임..
def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1): # 모든 값을 다 집어넣어봄..
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]