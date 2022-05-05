# 실패코드
# 왜이렇게 어렵게 생각할까
def solution(n, build_frame):
    def check_v(row, col):
        if row == n:  # 바닥에 있다는 얘기 이므로,
            return False
        if row < n and g[row + 1][col]:  # 내 밑에 체크(기둥)
            return True
        if row < n and col < n and g[row + 1][col + 1]:  # 내 오른쪽,밑에 체크 (기둥)
            return True
        if 1 <= col < n and v[row][col - 1] and v[row][col + 1]:  # 옆에 연결됐다면, (보)
            return True
        return False

    def check_g(row, col):
        if row == n:  # 바닥
            return True
        if row < n and g[row + 1][col]:  # 밑에 기둥
            return True
        if 1 < col and v[row][col - 1] == 1:  # and v[row][col-1] == 1: # 보의 오른쪽 끝에 존재함.
            return True
        if v[row][col] == 1:
            return True
            # if col == 0 or (1 < col and v[row][col-1] == 0): # 보의 왼쪽 끝에 존재함.
            #    return True
        return False

    g = [[0] * (n + 1) for _ in range(n + 1)]
    v = [[0] * (n + 1) for _ in range(n + 1)]

    for col, row, build, action in build_frame:
        row = n - row
        if action:  # 설치
            if build:  # 보
                if check_v(row, col):
                    v[row][col] = 1
            else:  # 기둥
                if check_g(row, col):
                    g[row][col] = 1

        else:  # 삭제
            flag = True
            if build:  # 보
                v[row][col] = 0
                if 1 <= col and v[row][col - 1]:  # 왼쪽 보의 상태
                    flag = check_v(row, col - 1)
                if flag and col < n and v[row][col + 1]:  # 오른쪽 보의 상태
                    flag = check_v(row, col + 1)
                if flag and g[row][col]:  # 바로 왼쪽 기둥의 상태
                    flag = check_g(row, col)
                if flag and col < n and g[row][col + 1]:  # 바로 오른쪽 기둥의 상태
                    flag = check_g(row, col + 1)
                if not flag:
                    v[row][col] = 1

            else:  # 기둥
                g[row][col] = 0
                if 1 <= row and v[row - 1][col]:
                    flag = check_v(row - 1, col)  # 오른쪽 보의 상태
                if flag and 1 <= row and 1 <= col and v[row - 1][col - 1]:  # 왼쪽 보의 상태
                    flag = check_v(row - 1, col - 1)
                if flag and 1 <= row and g[row - 1][col]:  # 위쪽 기둥의 상태
                    flag = check_g(row - 1, col)
                if not flag:
                    g[row][col] = 1
    # answer
    answer = []
    for col in range(n + 1):
        for i in range(n, -1, -1):
            row = n - i
            if g[i][col]:
                answer.append([col, row, 0])
            if v[i][col]:
                answer.append([col, row, 1])

    return answer

# 정답
# 와 그냥 있는 그대로 풀어버리니까 훨씬 쉽게 풀리네..
# 괜히 위에서 머리싸매는 것보다.. 훨씬 나은듯 싶다.
def solution(n, build_frame):
    def impossible(result):
        COL, ROW = 0, 1
        for x, y, a in result:
            if a == COL:
                if (y != 0) and (x, y, ROW) not in result and (x - 1, y, ROW) not in result and (
                x, y - 1, COL) not in result:
                    return True
            else:
                if (x, y - 1, COL) not in result and (x + 1, y - 1, COL) not in result and not (
                        (x - 1, y, ROW) in result and (x + 1, y, ROW) in result):
                    return True

        return False

    result = set()
    for x, y, a, build in build_frame:
        if build:
            result.add((x, y, a))
            if impossible(result):
                result.remove((x, y, a))
        else:
            result.remove((x, y, a))
            if impossible(result):
                result.add((x, y, a))

    result = map(list, result)
    return sorted(result, key=lambda x: (x[0], x[1], x[2]))
