a = input()
b = len(a)
odd_sum = 0
even_sum = 0
for i in map(int,a):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")