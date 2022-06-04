# import sys
# from io import StringIO
# test_input1 = '''1 2 3
# '''


# sys.stdin = StringIO(test_input1)


def sum_numbers(numbers):
    negative_sum = 0
    positive_sum = 0
    for n in numbers:
        if n < 0:
            negative_sum += n
        else:
            positive_sum += n

    return negative_sum, positive_sum


numbers = [int(x) for x in input().split()]

negative , positive = sum_numbers(numbers)

print(negative)
print(positive)

if abs(negative) > positive:
    print('The negatives are stronger than the positives')
else:
    print(f"The positives are stronger than the negatives")

