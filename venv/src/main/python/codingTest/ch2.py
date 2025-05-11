#01 두 수 비교하기
# instr = list(map(int, input().split(" ")))
# a, b = map(int, input().split(" "))
# if a>b: print('>')
# elif a<b: print('<')
# elif a==b: print("==")

# a, b = map(int, input().split())
# print('>' if a > b else '<' if a < b else '==')

# 02 점수
# testScore = int(input())
# print('A' if testScore>= 90
#     else 'B' if testScore>=80
#     else 'C' if testScore>=70
#     else 'D' if testScore>=60
#     else 'F')

# 03 윤년
# year = int(input())
#
# print(
#     '1' if (year%4==0 and (year%100!=0 or year%400==0))
#     else '0')

# 04 사분면 고르기
# def get_quadrant(x, y):
#     if x > 0 and y > 0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     else:
#         return 4
#
# def main():
#     x = int(input())
#     y = int(input())
#     print(get_quadrant(x, y))
#
# if __name__ == "__main__":
#     main()

# 05 알람시계
# inHour, inMin = map(int, input().split(" "))
#
# if inMin <= 45:
#     inHour -= 1
#     inMin += 60
#
# if inHour < 0:
#     inHour = 23
#
# resultHour = inHour
# resultMin = inMin - 45
#
# print(f"{resultHour} {resultMin}")

# a = 500
# print(int(a/60))

# 06 오븐 시계
# inHour, inMin = map(int, input().split(" "))
# cookingTime = int(input())
#
# totalMin = inHour*60 + inMin+cookingTime
#
# resultHour = (totalMin//60)%24
# resultMin = totalMin % 60
# print(f"{resultHour} {resultMin}")

# 주사위 세개
# nums = list(map(int, input().split()))
# max_value = max(nums)
# count = nums.count(max_value)
# print(count)
# if count==3:
#     print(10000+1000*max_value)
# elif count==2:
#     print(1000+100*max_value)
# elif count==1:
#     print(100*max_value)

nums = list(map(int, input().split()))
for n in nums:
    if nums.count(n) == 3:
        print(10000 + n * 1000)
        break
    elif nums.count(n) == 2:
        print(1000 + n * 100)
        break
else:
    print(max(nums) * 100)
