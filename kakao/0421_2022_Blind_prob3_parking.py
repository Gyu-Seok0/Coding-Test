#https://programmers.co.kr/learn/courses/30/lessons/92341

import collections
import math
def solution(fees, records):
    def cal(start, end):
        h1, m1 = int(start[:2]), int(start[3:]) #split보다는 indexing이 나음
        h2, m2 = int(end[:2]), int(end[3:])
        return (h2 - h1) * 60 + (m2 - m1)

    cars = collections.defaultdict(list)
    times = collections.defaultdict(int)
    for r in records:
        time, car, status = r.split()
        if status == "IN":
            cars[car] = [time]
        else:
            times[car] += cal(cars[car].pop(), time)

    # 남은 차 시간계산 이후 정산
    answer = []
    for car, time in sorted(cars.items()):  # 여기서 바로 sorted (중요한 부분)
        if time:
            times[car] += cal(time[0], "23:59")
        # 기본정산
        cars[car] = fees[1]
        # 추가정산
        if times[car] > fees[0]:
            cars[car] += math.ceil((times[car] - fees[0]) / fees[2]) * fees[3]
        # 정답추가 (중요부분)
        answer.append(cars[car])

    return answer