https://programmers.co.kr/learn/courses/30/lessons/42888
# 내풀이
def solution(record):
    id2name = dict()
    answer = []
    for r in record:
        action = r.split()[0]
        if action == "Leave":
            answer.append((r.split()[1], 1))
        else:
            _, b, c = r.split()
            id2name[b] = c
            if action == "Enter":
                answer.append((b, 0))

    express = ["님이 들어왔습니다.", "님이 나갔습니다."]
    return [id2name[id] + express[action] for id, action in answer]

#정답 -> 기능을 각각 구현한 점이 좋았다.
def solution(record):
    answer = []
    express = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'} # 이 부분도 dict로 풀이하는게 더 나을듯?
    d = dict()
    for r in record: # id update
        rr = r.split()
        if rr[0] in ["Enter", "Change"]:
            d[rr[1]] = rr[2]

    for r in record: #answer 추가
        rr = r.split()
        if rr[0] != "Change":
            answer.append(d[rr[1]] + express[rr[0]])

    return answer