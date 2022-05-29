import sys
from io import StringIO

test_input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''
# sys.stdin = StringIO(test_input1)



def matrix_create():
    n = int(input())
    matrix = []

    for _ in range(n):
        ll = []
        vals = input().split(", ")
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

primary_diagonal = []
secondary_diagonal = []
matrix = matrix_create()
finding_diagonals()

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(map(int, primary_diagonal))}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(map(int, secondary_diagonal))}")
