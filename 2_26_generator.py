import sys

def get_number():
    n = 0
    while True:
        n += 1
        yield n # generator 생성

g = get_number()  # 객체생성
for i in range(10):
    print(next(g)) #여기서 계속해서 실행

# generator가 훨씬 용량이 적은 것으로 보인다.
# 이유는 값을 다 가지고 있는게 아니라, 생성조건만 저장하고 있기 때문에 메모리가 훨씬 효율적이라고 할 수 있다.
print(f"size = {sys.getsizeof(([i for i in range(100)]))}")
print(f"size of generator = {sys.getsizeof(range(100))}")
