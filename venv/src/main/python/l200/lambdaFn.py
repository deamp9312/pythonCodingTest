# 두 수를 더하는 람다 함수
add = lambda x, y: x + y
print(add(3, 5))  # 8


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
