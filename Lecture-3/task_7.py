# import sys
# from io import StringIO

# test_input1 = '''5 6
# SoftUni
# '''

# test_input2 = '''1 4
# Python
# '''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)




rows, cols = [int(x) for x in input().split()]
word = input()
indx = 0
for row in range(rows):
    elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            elements[col] = word[indx % len(word)]
            indx += 1
    else:
        for col in range(cols - 1, -1, -1):
            elements[col] = word[indx % len(word)]
            indx += 1
    print(''.join(elements))