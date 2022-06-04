nums = input().split(" ")
copy_num = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_num)
    nums.remove(str(current_min_element))
    copy_num.remove(current_min_element)

print(', '.join(nums))