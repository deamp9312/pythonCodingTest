def decorator_function(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@decorator_function
def say_hello():
    print("Hello, World!")

say_hello()
# 출력:
# 함수 실행 전
# Hello, World!
# 함수 실행 후
