def fibonacci(num):
    if num <= 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num = fibonacci(1)
print(num)
num = fibonacci(2)
print(num)

