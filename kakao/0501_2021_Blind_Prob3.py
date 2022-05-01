# 풀이1: 기본
# 효율성이 실패함
def solution(info, query):
    answer = []
    # query를 하나씩 불러온다.
    for q in query:
        q = q.split(" and ")
        q += q.pop().split()
        cnt = 0
        # info에서 해당하는 사람들을 하나씩 카운트한다. -> 이부분이 코스트가 너무 많이 듦
        for i in info:
            a, b, c, d, e = i.split()
            if (q[0] == "-" or q[0] == a) and (q[1] == "-" or q[1] == b) and (q[2] == "-" or q[2] == c) and (
                    q[3] == "-" or q[3] == d) and int(e) >= int(q[4]):
                cnt += 1
        answer.append(cnt)

    return answer



# 풀이2 -> Binary Search가 요구됌.
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    global word, total

    word = {0: ["cpp", "java", "python"],
            1: ["backend", "frontend"],
            2: ["junior", "senior"],
            3: ["chicken", "pizza"]}

    def count(q):
        values = people[tuple(q[:4])]
        target = int(q[-1])
        l, r = 0, len(values)
        while l < r:
            mid = (l + r) // 2
            if values[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return len(values) - l
        # return len(values) - bisect_left(values, target)

    def dfs(index, q):
        global word, total
        for letter in word[index]:
            q[index] = letter
            if "-" in q:
                dfs(q.index("-"), q[:])
            else:
                total += count(q)

    # info를 통해 나올 수 있는 경우를 미리 정리하자.
    people = defaultdict(list)
    for i in info:
        people[tuple(i.split()[:4])].append(int(i.split()[-1]))

    for key, value in people.items():
        people[key] = sorted(value)

    # query를 하나씩 불러온다.
    answer = []
    for q in query:
        q = q.split(" and ")
        q += q.pop().split()
        total = 0
        if "-" in q:
            dfs(q.index("-"), q[:])
        else:
            total += count(q)

        answer.append(total)

    return answer


#풀이3 모든걸 다 기록..
#이런식으로 풀이가 가능하구나.

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list()) #이것도 진짜 신기함..
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        # Binary Search
        l,r = 0,len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer