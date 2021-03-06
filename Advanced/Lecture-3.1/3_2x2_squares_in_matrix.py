# import sys
# from io import StringIO

# test_input1 = '''5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# '''
# sys.stdin = StringIO(test_input1)

n , m= input().split(" ")

def matrix_create():
    matrix = []
    for _ in range(int(n)):
        ll = []
        vals = input().split(" ")
        for v in vals:
            ll.append(v)
    
        matrix.append(ll)

    return matrix

count = 0


# More complicated 

# def finding_square():
#     squares = []
    
#     for i in range(len(matrix)-1):
#         row = matrix[i]
#         for j in range(len(row)-1):
#             square = [
#                 [matrix[i][j]], [matrix[i][j+1]],
#                 [matrix[i+1][j]], [matrix[i+1][j+1]],
#             ]
#             squares.append(square)
    
#     overall_count = 0
#     for item in squares:
#         current_list = []
#         for char in item:
#             current_list.append(char[0])
#         if len(set(current_list)) == 1:
# #             overall_count += 1

#     return overall_count



def finding_square():
    squares = 0

    for row in range(int(n) - 1):
        for col in range(int(m) -1):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row +1][col + 1]:
                squares += 1

    return squares


primary_diagonal = []
secondary_diagonal = []
matrix = matrix_create()
print(finding_square())
