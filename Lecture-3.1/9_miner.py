direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def move(cell:tuple, direction:tuple) -> tuple:
    global matrix
    new_x = cell[0] + direction[0]
    new_y = cell[1] + direction[1]

    if 0 <= new_x < len(matrix):
        if 0 <= new_y < len(matrix[0]):
            return new_x, new_y
    else:
        return cell

def collect(cell:tuple) -> bool:
    global collected_coal
    row, col = cell
    symbol = matrix[row][col]
    if symbol == 'e':
        return False
    elif symbol == 'c':
        collected_coal += 1
        matrix[row][col] = '*'
    return True

size = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(size)]
starting_coal = 0
collected_coal = 0

for i, row in enumerate(matrix):
    starting_coal += row.count('c')    
    if 's' in row:
        position = (i, row.index('s'))

for command in commands:
    new_position = move(position, direction[command])
    if new_position:
        position = new_position
        if collect(position):
            game_over = False
            continue
        else:
            game_over = True
            break

if game_over:
    print(f"Game over! {position}")
elif collected_coal == starting_coal:
    print(f"You collected all coal! {position}")
else:
    print(f"{starting_coal - collected_coal} pieces of coal left. {position}")
    