dir = ((-1,0),(0,1),(1,0),(0,-1))

def A_turn(ar,ac,br,bc,cnt,board):
    if board[ar][ac] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = ar+dr,ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            board[ar][ac] = 0
            iswin,turn = B_turn(br,bc,nr,nc,cnt+1,board[:])
            board[ar][ac] = 1

            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def B_turn(br,bc,ar,ac,cnt,board):
    if board[br][bc] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = br+dr,bc+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            board[br][bc] = 0
            iswin,turn = A_turn(ar,ac,nr,nc,cnt+1,board[:])
            board[br][bc] = 1
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def solution(board, aloc, bloc):
    ar,ac,br,bc = aloc[0],aloc[1],bloc[0],bloc[1]
    answer = A_turn(ar,ac,br,bc,0,board)[1]
    return answer