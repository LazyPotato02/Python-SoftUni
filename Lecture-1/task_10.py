from collections import deque


cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))
wasted_litters_of_water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        cup -= bottle
    wasted_litters_of_water += abs(cup)

else:
    if cups:
        print(f"Cups:", ' '.join([str(x) for x in cups]))
    else:
        print(f"Bottles:", ' '.join([str(x) for x in bottles]))

    print(f"Wasted litters of water: {wasted_litters_of_water}")