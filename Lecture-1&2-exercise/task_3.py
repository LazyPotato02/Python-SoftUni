from collections import deque


chocolates = list(map(int, input().split(', ')))
cups = deque(map(int, input().split(', ')))
milkshakes = 0

while cups and chocolates:

    choco, cup = chocolates.pop(), cups.popleft()

    if min(choco, cup) <= 0: 
        if choco > 0: chocolates.append(choco)
        if cup > 0: cups.appendleft(cup)
        continue

    if choco == cup:
        milkshakes += 1
        if milkshakes == 5: break
    else:
        cups.append(cup)
        chocolates.append(choco - 5)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else: 
    print("Not enough milkshakes.")
if chocolates:
    print(f'Chocolate:', ', '.join(list(map(str, chocolates))))
else:
    print("Chocolate: empty")
if cups:
    print(f'Milk:', ', '.join(list(map(str, cups))))
else:
    print("Milk: empty")
    