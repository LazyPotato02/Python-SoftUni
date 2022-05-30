import sys
from io import StringIO

test_input1 = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''

test_input2 = '''5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


r , c= input().split(" ")


def matrix_create():
    matrix = []

    for _ in range(int(r)):
        ll = []
        vals = input().split(" ")
        for v in vals:
            ll.append(int(v))
    
        matrix.append(ll)

    return matrix


def finding_square(matrix):
    best_sum = float('-inf')
    start_row = 0
    start_col = 0
    matrix = matrix

    for row in range(int(r) - 2):
        for col in range(int(c) -2):
            current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
            if current_sum > best_sum:
                best_sum = current_sum
                start_row = row
                start_col = col
    
    return best_sum , start_row, start_col

def main():
    matrix = matrix_create()
    matrix_result = finding_square(matrix)
    total_sum = matrix_result[0]
    start_row = matrix_result[1]
    start_col = matrix_result[2]
    
    
    print(f"Sum = {total_sum}")
    print(f'{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}')
    print(f'{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}')
    print(f'{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}')

if __name__ == '__main__':
    main()