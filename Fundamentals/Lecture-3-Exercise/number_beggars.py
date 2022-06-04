# coins = [int(num) for num in input().split(", ")]
# beggars = int(input())
# count = 0
# beggars_list = [0] * beggars
# for coin in coins:
#     beggars_list[count] += coin
#     count += 1
#     if count >= beggars:
#         count = 0
# print(beggars_list) 


string = input().split(", ")
int_string = [int(x) for x in string]
beggars = int(input())
final_result = []
 
for current_beggar in range(beggars):
    current_sum = [0]
    current_sum += int_string[current_beggar:len(int_string):beggars]
    final_result.append(sum(current_sum))
print(final_result)
