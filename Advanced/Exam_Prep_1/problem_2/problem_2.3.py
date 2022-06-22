import sys
from io import StringIO

test_input_1 = '''
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)
'''.strip()

test_input_2 = '''
B 30 14 23 20 24
29 8 27 18 11 19
33 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
'''.strip()


sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)

def is_shot_in_matrix(row,col,ROW_MATRIX,COL_MATRIX):
    try:
        matrix_size = len(matrix)
        if row >= 0 and row <= matrix_size - 1 and col >= 0 and col <= matrix_size - 1:
            return True
    except:
        return False

ROW_MATRIX = 6
COL_MATRIX = 6

matrix = [input().split() for _ in range(ROW_MATRIX)]
points = 0

prices = {
    1: 'Football',
    2: 'Teddy Bear',
    3: 'Lego Construction Set'
}
for _ in range(3):
    shot = ''
    try:
        shot = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))
    except EOFError:
        break
    row, col = shot

    is_shot = is_shot_in_matrix(row,col,ROW_MATRIX,COL_MATRIX)
    if is_shot:
        sum_bucket = list()
        value = matrix[row][col]
        if value == 'B':
            matrix[row][col] == 0
            for i in range(0,6):
                if matrix[i][col].isnumeric():
                    v = matrix[i][col]
                    sum_bucket.append(v)
            
        for z in sum_bucket:
            points += int(z)


if points < 100:
    if points <= 0:
        print(f"Sorry! You need 100 points more to win a prize.")
    else:
        print(f"Sorry! You need {abs(100 - points)} points more to win a prize.")
elif points > 400:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
    print(f"Good job! You scored {points} points, and you've won {prices.get(points//100)}.")
