direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def move(cell:tuple, direction:tuple) -> tuple:
    global matrix
    x, y = cell
    matrix[x][y] = '.'

    new_x = x + direction[0]
    new_y = y + direction[1]

    if 0 <= new_x < rows:
        if 0 <= new_y < cols:
            if matrix[new_x][new_y] != 'B': 
                matrix[new_x][new_y] = 'P'
            return new_x, new_y
        else: return -1, -1
    else:
        return -1, -1

    
def bunny_spread() -> None:
    global matrix
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] not in ('B', 'b'):
                if row - 1 >= 0:
                    if matrix[row - 1][col] == 'B': matrix[row][col] = 'b'
                if row + 1 < rows:
                    if matrix[row + 1][col] == 'B': matrix[row][col] = 'b'
                if col - 1 >= 0:
                    if matrix[row][col - 1] == 'B': matrix[row][col] = 'b'
                if col + 1 < cols:
                    if matrix[row][col + 1] == 'B': matrix[row][col] = 'b'
    matrix = [['B' if x =='b' else x for x in y] for y in matrix]

rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append([x for x in input()])
    if 'P' in matrix[i]:
        row, col = i, matrix[i].index('P')
commands = [x for x in input()]

for command in commands:
    new_position = move((row, col), direction[command])
    bunny_spread()
    if new_position == (-1, -1):
        win = True  
        break
    else:
        row, col = new_position
        if matrix[row][col] == 'B':
            win = False
            break

for data in matrix:
    print(''.join(data))

if win:
    print(f"won: {row} {col}")
else:
    print(f"dead: {row} {col}")
