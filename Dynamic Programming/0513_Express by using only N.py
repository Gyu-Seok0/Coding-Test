#https://programmers.co.kr/learn/courses/30/lessons/42895
# 풀이: https://www.hamadevelop.me/algorithm-n-expression/
def solution(N, number):
    possible_set = [0,[N]]
    if N == number:
        return 1
    for i in range(2,9): # 2부터 8까지 숫자 증가
        case_set = set() # set으로 사용하는게 훨씬 효과적.
        basic_num = int(str(N)*i)
        case_set.add(basic_num)
        for i_half in range(1, i//2 +1): # 절반만 사용하면 됌.
            for x in possible_set[i_half]: # i_half + (i - i_half) = i가 나오는 쌍으로 풀이하면 됌.
                for y in possible_set[i - i_half]:
                    case_set.add(x+y)
                    case_set.add(x*y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    if y != 0:
                        case_set.add(x/y)
                    if x != 0:
                        case_set.add(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set)
    return -1