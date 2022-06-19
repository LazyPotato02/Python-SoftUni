import sys
from io import StringIO

test_input_1 = '''
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
right, up, up, up, up, left, left, left
'''.strip()

test_input_2 = '''
R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right
'''.strip()

test_input_3 = '''
R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left
'''.strip()

sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)


'''
• One rover - marked with the letter "E"
• Water deposit (one or many) - marked with the letter "W"
• Metal deposit (one or many) - marked with the letter "M"
• Concrete deposit (one or many) - marked with the letter "C"
• Rock (one or many) - marked with the letter "R"
• Empty positions will be marked with "-"
    
'''


def find_rover(matrix):
    # rover_cords = []

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_col = matrix[row][col]
            if current_col == 'E':
                # rover_cords.append((row,col))
                return row, col


def up(row):
    if row > 0:
        return row - 1
    else:
        row = ROWS_COUNT - 1
        return row


def down(row):
    if row < ROWS_COUNT - 1:
        return row + 1
    else:
        row = 0
        return row


def left(col):
    if col > 0:
        return col - 1
    else:
        col = COLUMNS_COUNT - 1
        return col

def right(col):
    if col < COLUMNS_COUNT - 1:
        return col + 1
    else:
        col = 0
        return col

def is_colony(found):
    if found["water"] >= 1 and found["metal"] >= 1 and found["concrete"] >= 1:
        return True


ROWS_COUNT = 6
COLUMNS_COUNT = 6

found = {
    "water" : 0,
    "metal" : 0,
    "concrete": 0,
}


matrix = [input().split() for _ in range(ROWS_COUNT)]
rover_movement = input().split(', ')
while rover_movement:

    row, col = find_rover(matrix)

    for move in rover_movement:
        if move == 'up':
            row = up(row)
        elif move == 'down':
            row = down(row)
        elif move == 'left':
            col = left(col)
        elif move == 'right':
            col = right(col)

        if matrix[row][col] == 'W':
            found["water"] += 1
            print(f"Water deposit found at ({row}, {col})")
        elif matrix[row][col] == "M":
            found["metal"] += 1
            print(f"Metal deposit found at ({row}, {col})")
        elif matrix[row][col] == "C":
            found["concrete"] += 1
            print(f"Concrete deposit found at ({row}, {col})")
        elif matrix[row][col] == "R":
            print(f"Rover got broken at ({row}, {col})")
            break

    is_done = is_colony(found)



    if is_done:
        print("Area suitable to start the colony.")
        break
    else:
        print("Area not suitable to start the colony.")
        break
