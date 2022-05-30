# import sys
# from io import StringIO

# test_input1 = '''4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
# '''
# sys.stdin = StringIO(test_input1)


def matrix_create():
    n = int(input())
    matrix = []

    for _ in range(n):
        ll = []
        vals = input().split(" ")
        for v in vals:
            ll.append(v)
    
        matrix.append(ll)

    return matrix


def finding_diagonals():
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            n = len(matrix)
            if x == y:
                primary_diagonal.append(matrix[x][y])
            if x == n - y -1:
                secondary_diagonal.append(matrix[x][y])


def printing():
    primary_diag_sum = sum(map(int, primary_diagonal))
    secondary_diag_sum = sum(map(int, secondary_diagonal))
    difference = abs(primary_diag_sum - secondary_diag_sum)

    print(difference)


primary_diagonal = []
secondary_diagonal = []
matrix = matrix_create()
finding_diagonals()
printing()
