intersections = []
max_len = 0
for _ in range(int(input())):
    range_1, range_2 = input().split('-')
    x1, x2 = range_1.split(',')
    y1, y2 = range_2.split(',')
    set_x = set([x for x in range(int(x1), int(x2) + 1)])
    set_y = set([y for y in range(int(y1), int(y2) + 1)])
    intersection = set_x & set_y
    intersections.append((list(intersection), len(intersection)))
    max_len = max(len(intersection), max_len)

output = next(filter(lambda x: x[1] == max_len, intersections))
print(f"Longest intersection is {output[0]} with length {output[1]}")
