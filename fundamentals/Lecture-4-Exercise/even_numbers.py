a = input().split(" ")


def check_even(a):
    if int(a) % 2 == 0:
          return True  

    return False

even_numbers_iterator = filter(check_even, a)
even_numbers = list(even_numbers_iterator)

for i in range(0, len(even_numbers)):
    even_numbers[i] = int(even_numbers[i])

print(even_numbers)
