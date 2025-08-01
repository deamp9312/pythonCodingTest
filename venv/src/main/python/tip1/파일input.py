# input
# sys.stdin.readline
# 이때는 맨 끝의 개행문자까지 같이 입력받기
# 때문에 문자열을 저장하고 싶을 경우
# .rstrip()을 추가로 해 주는 것이 좋다.


import sys
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    A, B = map(int, input().split())
    results.append(str(A + B))

sys.stdout.write("\n".join(results))


# 예시
#빠른 A+B
import sys

input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    A,B = map(int,input().split())
    result.append(f"Case #{i+1}: {A + B}")

sys.stdout.write("\n".join(result))