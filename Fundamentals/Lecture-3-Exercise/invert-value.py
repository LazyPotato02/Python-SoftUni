# Method 1 -------------------------------------
# a = input().split(" ")
# new_list = []

# for n in a:
#     if int(n) > 0:
#         new_list.append(-int(n))
#     else:
#         new_list.append(abs(int(n)))

# print(new_list)


# Method 2 ------------------------------------- List comprehation

# nums = [-num if num > 0 else abs(num) for num in list(map(int,input().split(" ")))]
# print(nums)