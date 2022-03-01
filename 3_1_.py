# 내 풀이: 부르트 포스 -> 시간초과
class Solution:
    def check(self, s):
        return s[::-1] == s

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_pal = ""
        for start in range(len(s)):
            for end in range(start, len(s) + 1):
                if end - start + 1 > max_length:
                    if self.check(s[start:end]):
                        max_pal = s[start:end]
                        max_length = end - start + 1
        return max_pal

# 교재풀이: 투포인터 사용
def expand(left:int, right: int) -> str:
    while left >=0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

    # 예외처리
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key = len)
    return result

# LCS(longest Common Substring) -> DP로 문제풀이
# 이 방식은 두개의 문자열 사이의 공통 부분을 찾기 때문에 알고리즘적으로 다르다.
s = "aacabdkacaa"
s_reverse = s[::-1] #"aacakdbacaa" 4
dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
m = ""
for i in range(len(s)):
    for j in range(len(s_reverse)):
        if s[i] == s_reverse[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            start = len(s) - j - 1
            end = i+1
            if len(m) < end - start + 1:
                m = s[start:end]
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
for row in range(len(dp)):
     for col in range(len(dp)):
         print(dp[row][col], end = " ")
     print("\n")
print(m)



