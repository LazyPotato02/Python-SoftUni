# import sys
# from io import StringIO

# test_input1 = '''3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# '''


# sys.stdin = StringIO(test_input1)

size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])


while True:

    line = input()

    if line == 'END':
        break

    parts = line.split()
    command = parts[0]
    row, col, value = [int(x) for x in parts[1:]]

    if row < 0 or col < 0 or row >= size or col >= size:
        print("Invalid coordinates")
        continue

    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')