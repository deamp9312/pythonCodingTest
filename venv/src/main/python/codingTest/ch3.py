# 구구단
# gugudan = int(input())
#
# for i in range(1,10):
#     print(f"{gugudan} * {i} = {gugudan*i}")


# A + B -3
# rangeI = int(input())
#
# for i in range(rangeI):
#     a,b = map(int, input().split())
#     print(a+b)

# 합
# def factory(num: int) -> int:
#     result = 0
#     for i in range(1,num+1):
#         result += i
#     return result
#
# print(factory(int(input())))

# 영수증
# totalMony = int(input())
# totalCount = int(input())
# resultMont = 0
# for _ in range(totalCount):
#     mony , count = map(int,input().split())
#     resultMont += mony*count
#
# if totalMony==resultMont:
#     print("Yes")
# else:
#     print("No")

#빠른 A+B
# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
# result = []
#
# for i in range(T):
#     A,B = map(int,input().split())
#     result.append(f"Case #{i+1}: {A + B}")
#
# sys.stdout.write("\n".join(result))

# 별 찍기
# import sys
#
# def star(a: int)-> str:
#     if a==1:
#         return "*"
#     return "*"+star(a-1)

# input = sys.stdin.readline
# result = []
# for i in range(int(input())):
#     result.append(f"{star(i+1)}")
#
# sys.stdout.write("\n".join(result))

#별 오른쪽 정렬

# input = sys.stdin.readline
# result = []
# N = int(input())
# for i in range(1,N+1):
#     result.append(" "*(N-i)+"*"*i)
#
# sys.stdout.write("\n".join(result))

# a+b -5 while 문제
import sys

input = sys.stdin.readline
result = []

while True:
    a,b = map(int, input().split())
    if a==0 and b ==0:
        break
    result.append(f"{a+b}")
sys.stdout.write("\n".join(result))