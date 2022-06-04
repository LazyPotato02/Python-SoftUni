num_1 = int(input())
num_2 = int(input())
new_list = []

for num in range(1, num_2 + 1):
    new_list.append(num * num_1)

print(new_list)