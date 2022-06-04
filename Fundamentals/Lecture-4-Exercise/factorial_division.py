def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)

num_1 = int(input())
num_2 = int(input())

result = factorial(num_1) / factorial(num_2)
print(f"{result:.2f}")