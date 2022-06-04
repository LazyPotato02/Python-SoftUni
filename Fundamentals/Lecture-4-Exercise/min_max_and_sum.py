a = list(map(int,input().split(" ")))
max_num = max(a)
min_num = min(a)

def sum_of_nums(a):
    sum_1 = 0
    for i in a:
        sum_1 += i
    print(f"The sum number is: {sum_1}")


print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
sum_of_nums(a)