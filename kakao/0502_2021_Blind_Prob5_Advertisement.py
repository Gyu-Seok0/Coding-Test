# 시간초과 코드
# https://programmers.co.kr/learn/courses/30/lessons/72414
def solution(play_time, adv_time, logs):
    def change(time):
        time = time.split(":")
        left, result = 0, 0
        idx = 2
        while idx >= 0:
            if idx != 0:
                left, mod = divmod(int(time[idx]) + left, 60)
            else:
                mod = int(time[idx]) + left
            result += mod * (60 ** (2 - idx))
            idx -= 1
        return result

    def translate(t):
        idx = 0
        times = []
        while idx < 3:
            cal, t = divmod(t, 60 ** (2 - idx))
            if len(str(cal)) < 2:
                times.append("0" + str(cal))
            else:
                times.append(str(cal))
            idx += 1
        return ":".join(times)

    # logs로 start, end형태로 계산
    watch = []
    for log in logs:
        watch.append(list(map(lambda x: change(x), log.split("-"))))
    watch.sort(key=lambda x: x[0])

    # start위치마다 계산하면 될듯?
    adv_time = change(adv_time)
    play_time = change(play_time)
    total, video = 0, 0
    # print("watch",watch)
    for idx, (start, end) in enumerate(watch):
        time = 0
        # 끝나는 시간 더하기
        target = start + adv_time
        # 시간을 초과
        if target > play_time:
            start -= target - play_time
            target = play_time

        # print("start,target",start,target)
        for next_start, next_end in watch:
            if next_start >= target:  # 범위 초과
                break
            elif next_end <= start:  # 범위 미만
                continue
            else:
                time += min(next_end, target) - max(next_start, start)

        if time > total:
            total, video = time, start

    return translate(video)

# 정답코드
def solution(play, adv, logs):
    def str2int(time):
        return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])

    def int2str(num):
        hour, num = divmod(num, 3600)
        min, sec = divmod(num, 60)
        return "{:0>2}:{:0>2}:{:0>2}".format(hour, min, sec)

    play, adv = str2int(play), str2int(adv)
    print(play, adv)
    time = [0] * (play + 1)

    for log in logs:
        start, end = map(lambda x: str2int(x), log.split("-"))
        time[start] += 1
        time[end] -= 1

    for i in range(1, play):
        time[i] += time[i - 1]

    for i in range(1, play):
        time[i] += time[i - 1]

    result, people = 0, time[adv]
    for i, j in zip(range(play + 1 - adv), range(adv, play + 1)):  # 투포인터 사용(i와 j가 adv만큼 차이남)
        if people < time[j] - time[i]:  # j시간에 본 사람 - i시간에 본 사람 = (i+1 ~ j시간까지 시청한 누적시청자)
            result, people = i + 1, time[j] - time[i]  # 참고: 시간 i의 의미는 i시간을 기준으로 시청한 사람을 의미한다.

    return int2str(result)