a, b, c = int(input()), int(input()), int(input())

def sum_numbers(a,b):
    return a + b

def substract(c):
    return sum_numbers(a,b) - c

def add_and_substract(a,b,c):
    sum_numbers(a,b)
    return substract(c)

print(add_and_substract(a,b,c))