clothes = list(map(int, input().split()))
capacity = int(input())
racks = 1
clothes_on_rack = 0

while clothes:
    item = clothes.pop()
    if item <= capacity - clothes_on_rack:
        clothes_on_rack += item
    else:
        clothes_on_rack = item
        racks += 1

print(racks)
