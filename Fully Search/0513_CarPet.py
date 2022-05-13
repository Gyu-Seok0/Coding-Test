# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for i in range(1, yellow+1):
        j, rest = divmod(yellow,i)
        if rest == 0:
            if (j+2) * (i+2) - yellow == brown:
                return [j+2,i+2]