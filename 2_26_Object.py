# 파이썬은 모든 것이 객체이다. Str도 INT도 이미 어딘가에 선언이 되어있고, 변수들을 이것들을 그저 참조할 따름이다.
# 그리고 이러한 객체들은 가변객체와 불변객체가 있는데, 가변객체로는 리스트-SET-DICT가 있다.

a = 10
b = a
print(id(a), id(b), id(10))

a = 11
b = 11
print(id(a), id(b), id(11))


temp = [1 for _ in range(5)]
print(f"Before {temp}")

# DEL
del temp[1] # temp에서 1번째 요소를 제거하자.
print(f"after {temp}")

