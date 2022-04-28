def solution(new_id):
    temp = new_id.lower()  # 1 lower

    # 2
    answer = ""
    for letter in temp:
        if letter.isalnum() or letter in ["_", "-", "."]:
            answer += letter
    # 3
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4
    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[:-1]

    # 5
    if answer == "":
        answer = "a"
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer