https://programmers.co.kr/learn/challenges
# 1번문제
# 주어진 문자열(문자와 숫자의 조합)을 문자로 표현하기
# replace사용하면 되는구나.

# 내풀이
def solution(s):
    dic = {"ze": ["0", 4], "on": ["1", 3], "tw": ["2", 3], "th": ["3", 5], "fo": ["4", 4],
           "fi": ["5", 4], "si": ["6", 3], "se": ["7", 5], "ei": ["8", 5], "ni": ["9", 4]}

    answer = ""
    # s를 하나씩 읽기
    while s:
        value = s[0]
        if value.isnumeric():
            answer += value
            s = s[1:]

        else:
            num, length = dic[s[:2]]
            answer += num
            s = s[length:]

    return int(answer)

# answer
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# 2번문제
# 거리두기를 잘하고 있는지 확인 (맨해튼 거리가 무조건 2를 초과해야 하고, 거리가2인경우 파티션으로 나눠져야 한다)
# FLAG를 두어서 inner, middle for문을 멈춰줬었는데, 그냥 함수형태로 return해주는게 훨씬 깔끔했다.

def solution(places):
    # 오른쪽1, 오른쪽2, 아래1, 아래2, 아래1+오른쪽1, 아래1+왼쪽1
    answer = []

    def check(room):
        for row in range(5):
            for col in range(5):
                if room[row][col] != "P":
                    continue
                if col + 1 < 5 and room[row][col + 1] == "P":
                    return 0
                if col + 2 < 5 and room[row][col + 2] == "P" and room[row][col + 1] != "X":
                    return 0
                if row + 1 < 5 and room[row + 1][col] == "P":
                    return 0
                if row + 2 < 5 and room[row + 2][col] == "P" and room[row + 1][col] != "X":
                    return 0
                if row + 1 < 5 and col + 1 < 5 and room[row + 1][col + 1] == "P":
                    if room[row + 1][col] != "X" or room[row][col + 1] != "X":
                        return 0
                if row + 1 < 5 and col - 1 >= 0 and room[row + 1][col - 1] == "P":
                    if room[row + 1][col] != "X" or room[row][col - 1] != "X":
                        return 0
        return 1

    return [check(place) for place in places]

#3번문제
# 표편집문제 -> Linked list를 적절히 활용하기
# https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python
def solution(n, cur, cmd):
    # table
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]

    # stack
    stack = []

    # answer
    answer = ["O"] * n

    # cmd
    for c in cmd:
        if c == "C":
            answer[cur] = "X"
            prev, next = table[cur]
            stack.append([prev, cur, next])

            # cur
            if next == None:
                cur = prev  # 전에 위치
            else:
                cur = next  # 다음에 위치

            # linked list
            if prev == None:  # 가장 처음에 위치했다면
                table[next][0] = None
            elif next == None:  # 가장 마지막에 위치
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            prev, now, next = stack.pop()
            answer[now] = "O"
            if prev == None:  # 가장 상위
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[prev][1] = now
                table[next][0] = now
        else:
            c1, c2 = c.split(" ")
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]

            else:
                for _ in range(c2):
                    cur = table[cur][0]

    return ''.join(answer)