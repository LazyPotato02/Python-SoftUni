# import sys
# from io import StringIO

# test_input1 = '''4 6
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# '''

# test_input2 = '''3 2
# '''

# # sys.stdin = StringIO(test_input1)
# # sys.stdin = StringIO(test_input2)




rows, cols = [int(x) for x in input().split()]

chars = 'abcdefghijklmnopqrstuvwxyz'

for i in range(rows):
    row = [f'{chars[i]}{chars[j]}{chars[i]}' for j in range(i, cols + i)]
    print (*row, sep=' ')