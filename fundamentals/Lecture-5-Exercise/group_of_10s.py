from math import ceil

input_nums = list(map(int,input().split(', ')))

for i in range(1, ceil(max(input_nums) / 10) + 1):
    group = list(filter(lambda x: (i - 1) * 10 < x <= i * 10, input_nums))
    print (f"Group of {i}0's: {group}")