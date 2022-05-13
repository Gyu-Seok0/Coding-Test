#https://programmers.co.kr/learn/courses/30/lessons/72415

from collections import deque
def solution(board, r, c):
    answer = 0
    board = "".join(str(each) for row in board for each in row) # string으로 체킹이 가능하다.
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) # 디렉션을 미리 설정해놓는다.
    que = deque([(r, c, 0, -1, board)])  # y,x,count,enter,board for bfs
    visited = set() # visited 설정하기

    while que:
        y, x, count, enter, board = que.popleft()
        if board.count('0') == 16:  # end
            return count
        if (y, x, enter, board) in visited:
            continue
        visited.add((y, x, enter, board))

        # 현 위치에서 갈 수 있는 모든 방향으로 이동(한칸씩 or ctrl)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                que.append((ny, nx, count + 1, enter, board))
            ny, nx = ctrl_move(y, x, dy, dx, board)
            if ny == y and nx == x:
                continue
            que.append((ny, nx, count + 1, enter, board))

        # check
        position = y * 4 + x
        if board[position] != "0":
            if enter == -1:
                que.append((y, x, count + 1, position, board))  # enter 누름
            elif enter != position and board[enter] == board[position]: # enter를 누른 위치와 현 postion이 다르고, 두 개의 값이 같다면,
                board = board.replace(board[enter], "0") # 다 zero로 만듬.
                que.append((y, x, count + 1, -1, board))


def ctrl_move(y, x, dy, dx, board):
    ny, nx = y + dy, x + dx
    if 0 <= ny < 4 and 0 <= nx < 4:
        if board[ny * 4 + nx] == "0":
            return ctrl_move(ny, nx, dy, dx, board) # recursive로 계속 탐색.
        else:
            return ny, nx
    else:
        return y, x