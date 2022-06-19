import sys
from io import StringIO

test_input_1 = '''
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End
'''.strip()

test_input_2 = '''
5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3
'''.strip()

test_input_3 = '''
5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End
'''.strip()

sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)


def printing():
    print('You\'ve collected:')
    for k, v in found.items():
        print(f'- {v} {k}')


def find_santa(matrix):

    for row in range(0, ROWS_COUNT):
        for col in range(0, COLUMNS_COUNT):
            current_col = matrix[row][col]
            if current_col == 'Y':
                return row, col


def check_is_find(row, col):
    if matrix[row][col] == 'D':
        found["Christmas decorations"] += 1
    elif matrix[row][col] == 'G':
        found['Gifts'] += 1
    elif matrix[row][col] == 'C':
        found['Cookies'] += 1


def is_all_connecter():
    for row in range(ROWS_COUNT):
        for col in range(COLUMNS_COUNT):
            if matrix[row][col] == 'D' or matrix[row][col] == 'G' or matrix[row][col] == 'C':
                return False
    return True


def up(row, moves, col, R_COUNT):
    for i in range(moves):
        if row - 1 >= 0:
            matrix[row][col] = 'x'
            row = row - 1
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break
        else:
            matrix[row][col] = 'x'
            R_COUNT = R_COUNT - 1
            row = R_COUNT
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break


def down(row, moves, col, R_COUNT):
    for i in range(moves):
        if row + 1 <= R_COUNT - 1:
            matrix[row][col] = 'x'
            row = row + 1
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break
        else:
            matrix[row][col] = 'x'
            row = R_COUNT - R_COUNT
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break


def left(col, moves, row, C_COUNT):
    for i in range(moves):
        if col - 1 >= 0:
            matrix[row][col] = 'x'
            col = col - 1
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break
        else:
            matrix[row][col] = 'x'
            col = C_COUNT - 1
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break


def right(col, moves, row, C_COUNT):
    for i in range(moves):
        if col + 1 <= C_COUNT - 1:
            matrix[row][col] = 'x'
            col = col + 1
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break
        else:
            matrix[row][col] = 'x'
            col = 0
            check_is_find(row, col)
            matrix[row][col] = 'Y'
            is_empty = is_all_connecter()
            if is_empty:
                print("Merry Christmas!")
                break


matrix_cords = input().split(', ')

ROWS_COUNT = int(matrix_cords[0])
COLUMNS_COUNT = int(matrix_cords[1])
matrix = [input().split() for _ in range(ROWS_COUNT)]


found = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}


while True:
    R_COUNT = ROWS_COUNT
    C_COUNT = COLUMNS_COUNT
    try:
        commands = input()
    except EOFError:
        break

    if commands == 'End':
        break

    commands = commands.split('-')

    command = commands[0]
    moves = int(commands[1])
    row, col = find_santa(matrix)
    if command == 'up':
        row = up(row, moves, col, R_COUNT)
    elif command == 'down':
        row = down(row, moves, col, R_COUNT)
    elif command == 'left':
        col = left(col, moves, row, C_COUNT)
    elif command == 'right':
        col = right(col, moves, row, C_COUNT)

printing()
for row in matrix:
    print(' '.join(row))
