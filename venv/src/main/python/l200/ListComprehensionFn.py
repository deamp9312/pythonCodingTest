# 1부터 10까지의 제곱수를 담은 리스트 만들기
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 1부터 10까지의 짝수의 제곱수를 담은 리스트 만들기
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
