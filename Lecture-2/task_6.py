odd_nums = set()
even_nums = set()

for i in range(1, int(input()) + 1):
    sum_ascii = sum([ord(x) for x in input()])
    num = sum_ascii // i
    if num % 2 == 0:
        even_nums.add(num)
    else:
        odd_nums.add(num)

sum_odd, sum_even = sum(odd_nums), sum(even_nums)

if sum_odd == sum_even:
    print(', '.join([str(x) for x in even_nums.union(odd_nums)]))
elif sum_odd > sum_even:
    print(', '.join([str(x) for x in odd_nums.difference(even_nums)]))
else:
    print(', '.join([str(x) for x in even_nums.symmetric_difference(odd_nums)]))
    