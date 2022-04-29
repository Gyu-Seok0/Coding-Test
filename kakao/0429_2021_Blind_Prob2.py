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