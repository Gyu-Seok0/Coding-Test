# 1. 단어를 개수별로 정리한다. + (이때, Reversed form으로도 정리함)
# 2. 단어를 sort시킨다
# 3. 쿼리문을 binary search로 돌려서 개수를 확인한다.


from bisect import bisect_left,bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

array = [[] for i in range(10001)]
reversed_array = [[] for i in range(10001)]
def solution(words, queries):
    answer = []
    for word in words:
        #단어 개수별로 정리
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) # 거꾸로

    # 단어들을 sorting
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != "?": #접미사라는 얘기지
            res = count_by_range(array[len(q)], q.replace("?",chr(96)), q.replace("?",chr(123)))
        else: #뒤에서 부터 세는게 힘드니까, 의부로 뒤집어서 시작해놓음
            res = count_by_range(reversed_array[len(q)], q[::-1].replace("?",chr(96)), q[::-1].replace("?",chr(123)))
        answer.append(res)
    return answer