# 내풀이가 제일 좋아보인다?
from collections import deque
def solution(board):
    answer = 0
    N = len(board)
    block = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                block.add((i + 1, j + 1))

    visited = set()
    start = (1, 1, 1, 2, 0)
    q = deque([start])
    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if x1 < 1 or x1 > N or x2 < 1 or x2 > N or y1 < 1 or y1 > N or y2 < 1 or y2 > N:  # 범위 초과
            continue
        if (x1, y1) in block or (x2, y2) in block or (x1, y1, x2, y2) in visited:  # Block이거나 방문한적 있다면,
            continue
        # 종료 (x1,y1) or (x2,y2)가 block에 있을 수도 있으므로 종료조건을 나중에 쓰는게 좋다.
        if (N, N) in [(x1, y1), (x2, y2)]:
            return cnt
        visited.add((x1, y1, x2, y2))

        q.append([x1, y1 - 1, x2, y2 - 1, cnt + 1])  # 좌
        q.append([x1, y1 + 1, x2, y2 + 1, cnt + 1])  # 우
        q.append([x1 - 1, y1, x2 - 1, y2, cnt + 1])  # 상
        q.append([x1 + 1, y1, x2 + 1, y2, cnt + 1])  # 하

        # 가로방향
        if x1 == x2:
            if (x1 - 1, y1) not in block and (x2 - 1, y2) not in block:
                q.append([x1 - 1, y1, x1, y1, cnt + 1])
                q.append([x2 - 1, y2, x2, y2, cnt + 1])

            if (x1 + 1, y1) not in block and (x2 + 1, y2) not in block:
                q.append([x1, y1, x1 + 1, y1, cnt + 1])
                q.append([x2, y2, x2 + 1, y2, cnt + 1])
        # 세로방향
        else:
            if (x1, y1 - 1) not in block and (x2, y2 - 1) not in block:
                q.append([x1, y1 - 1, x1, y1, cnt + 1])
                q.append([x2, y2 - 1, x2, y2, cnt + 1])

            if (x1, y1 + 1) not in block and (x2, y2 + 1) not in block:
                q.append([x1, y1, x1, y1 + 1, cnt + 1])
                q.append([x2, y2, x2, y2 + 1, cnt + 1])