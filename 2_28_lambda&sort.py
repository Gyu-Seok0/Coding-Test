from typing import List

# 내 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자인지, 숫자인지 구분하기
        digit_list = []
        let_tuple = []
        for idx, log in enumerate(logs):
            log_split = log.split()

            if log_split[1].isnumeric():
                digit_list.append(log)
            else:
                let_tuple.append((log_split[0], " ".join(log_split[1:])))

        let_sort = sorted(let_tuple, key=lambda x: (x[1], x[0]))
        let_list = []
        for item in let_sort:
            let_list.append(item[0] + " " + item[1])

        return let_list + digit_list

# 정답 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        #letters = sorted(letters, key = lambda x: (x.split()[1:], x.split()[0]))
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

'''
전체적인 로직은 비슷했는데, 코드의 간결성 측면에서 나보다 훨씬 나았다. 앞으로 이런 코드를 짜도록 유념하자.
내일은 
'''
