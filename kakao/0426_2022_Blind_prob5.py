#https://programmers.co.kr/learn/courses/30/lessons/92343
def solution(info, edges):
    global answer
    N = len(info)
    graph = [[] for _ in range(N)]
    for parent, child in edges:
        graph[parent].append(child)

    def search(visited, sheep, wolf):
        global answer
        # 종료조건1: 죽음 or 종료조건2: 다돌았음
        if wolf >= sheep or len(visited) == N:
            answer = max(answer, sheep)
            return

        # 돌기
        for parent in visited:
            for child in graph[parent]:
                if child not in visited:
                    if info[child] == 0:
                        search(visited + [child], sheep + 1, wolf)
                    else:
                        search(visited + [child], sheep, wolf + 1)

    answer = 1
    search([0], 1, 0)
    return answer

#5번문제
# 시간초과
def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if type == 1:
                    board[row][col] -= degree
                else:
                    board[row][col] += degree
    answer = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] > 0:
                answer += 1

    return answer

# 누적합 문제
def solution(board, skill):
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    # 마킹하기
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        temp[r1][c1] += degree
        temp[r1][c2 + 1] -= degree
        temp[r2 + 1][c1] -= degree
        temp[r2 + 1][c2 + 1] += degree

    # 가로방향으로 진행(0번째 row)
    for j in range(len(temp[0]) - 1):
        temp[0][j + 1] += temp[0][j]

    # 세로방향으로 진행(0번째 column)
    for i in range(len(temp) - 1):
        temp[i + 1][0] += temp[i][0]

    # cal
    answer = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == 0 or col == 0:
                pass
            else:
                temp[row][col] += temp[row - 1][col] + temp[row][col - 1] - temp[row - 1][col - 1]

            if board[row][col] + temp[row][col] > 0:
                answer += 1

    return answer