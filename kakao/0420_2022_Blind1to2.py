# 신고를 해서, 내가 신고한 사람이 정지될 경우 메일을 받는다.
# 각 유저별로 받게 되는 메일의 횟수를 리턴하면 되는 문제였다.
# k라는 조건을 빼먹어서 애를 먹었었다.. 항상 문제를 제대로 읽을 필요가 있다.
# report를 set으로 줄여주는게 좋은것 같다.
import collections
def solution(id_list, report, k):
    singo = collections.defaultdict(list)
    for r in report:
        value, key = r.split()
        singo[key].append(value)
        singo[key] = list(set(singo[key]))
    count = {i: 0 for i in id_list}

    for key, value in list(singo.items()):
        if len(value) >= k:
            for name in value:
                count[name] += 1
    return list(count.values())


from collections import OrderedDict
def solution(id_list, report, k):
    singo, count = {}, OrderedDict()
    for id in id_list:
        singo[id] = []
        count[id] = 0

    for r in report:
        val, key = r.split(" ")
        if val not in singo[key]:
            singo[key].append(val)

    for key, value in singo.items():
        if len(value) >= k:
            for name in value:
                count[name] += 1

    return list(count.values())

# solution -> 아무래도, for문을 두번 돌면서 훨씬 나은 점수를 받는 것 같다.. 이건 배워야 한다.
# set
# index
# split()[0], [1]

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    # 신고 체크
    for r in set(report):
        reports[r.split()[1]] += 1
    # 정답확인
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# 다시풀어봄
import collections
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = collections.defaultdict(set)
    # 신고 체크
    for r in set(report):
        value, key = r.split()
        reports[key].add(value)

    for key, value in list(reports.items()):
        if len(value) >= k:
            for name in value:
                answer[id_list.index(name)] += 1

    return answer


# 2번문제: K진수에서 소수개수 구하기
import math
def solution(n, k):
    def find(num):
        if num < 2:
            return 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 1

    # 변환하기
    change = ""
    while n > 0:
        n, r = divmod(n, k)
        change = str(r) + change

    # 앞에서부터 확인하기
    left, right, answer = 0, 0, 0
    for idx, value in enumerate(change):
        if value == "0":
            right = idx
            answer += find(int(change[left:right]))
            left = right
    if left == right:
        answer += find(int(change[left:]))

    return answer
# 내풀이가 조금더 복잡해보이지만, 효율성 측면에서 더 나은 점수를 받았다.

# solution
def solution(n, k):
    def is_prime(num):
        if num < 2:
            return 0
        i = 2
        while i * i <= num: # sqrt쓰는것보다 이렇게 표현하는게 더 쉬울 듯 싶다.
            if num % i == 0:
                return 0
            i += 1
        return 1

    # 변환하기
    change = ""
    while n > 0:
        n, r = divmod(n, k)
        change = str(r) + change

    # 앞에서부터 확인하기
    left, right, answer = 0, 0, 0
    for num in change.split("0"): # split()를 쓰면 훨씬 쉽게 풀이가 가능하다.
        if not num:
            continue
        answer += is_prime(int(num))
    return answer