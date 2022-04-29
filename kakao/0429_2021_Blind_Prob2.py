# 문제: https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    # order들 각각에 대한 조합을 만든다. 그 조합을 카운트하면 될듯 싶다.
    answer = []
    for num_food in course:
        dict = defaultdict(int)
        for order in orders:
            for food in list(combinations(sorted(list(order)), num_food)):
                dict[food] += 1

        if len(dict) == 0:
            continue

        max_value = max(dict.values())
        if max_value < 2:
            continue

        for menu, cnt in list(dict.items()):
            if cnt == max_value:
                answer.append("".join(menu))

    # 맨마지막에 CNT가 2이상인 것들안에서 ORDER BY시키면 될것 같다.
    return sorted(answer)


from itertools import combinations
from collections import Counter

# 정답풀이
# Counter, most_common 사용에 대해 알게됌 -> 사실 이것보다 아래 부분이 더 많이 알게 됌
# 일단 combinations는 리스트형태로 반환된다는 점을 알게 됌.
# Counter를 쓰는 것도 매우 좋은 전략이라고 파악 됌.

def solution(orders, course):
    # order들 각각에 대한 조합을 만든다. 그 조합을 카운트하면 될듯 싶다.
    answer = []
    for num_food in course:
        result = []
        for order in orders:
            result += combinations(sorted(order), num_food)  # 모든 조합이 다 모임.
        if not result:
            continue

        most = Counter(result).most_common() # 최빈값을 이용하면 쉽게 풀이가 가능, 괄호안에 k개를 넣으면, k개의 상위 최빈값에 해당하는 key와 최반값을 반환해줌.
        if most[0][1] < 2:
            continue

        answer += ["".join(key) for key, cnt in most if cnt == most[0][1]]

    # 맨마지막에 CNT가 2이상인 것들안에서 ORDER BY시키면 될것 같다.
    return sorted(answer)


# 개선된 풀이.
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    # order들 각각에 대한 조합을 만든다. 그 조합을 카운트하면 될듯 싶다.
    answer = []
    for num_food in course:
        dict = defaultdict(int)
        for order in orders:
            for food in combinations(sorted(order), num_food): # sorted로 기존에 list로 묶은형태를 없앰. order.sort()는 불가하다는 거 이해하기.
                dict[food] += 1

        if len(dict):
            max_value = max(dict.values())
            if max_value >= 2:
                for menu, cnt in sorted(dict.items(), key=lambda x: x[1], reverse=True): # value기준으로 정렬시킴
                    if cnt == max_value:
                        answer.append("".join(menu))
                    else:
                        break

                # answer += ["".join(menu) for menu, cnt in list(dict.items()) if cnt == max_value]

    # 맨마지막에 CNT가 2이상인 것들안에서 ORDER BY시키면 될것 같다.
    return sorted(answer)
