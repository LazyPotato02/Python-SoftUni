import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

test_input2 = '''3
1 2 3
4 5 6
7 8 9
'''


sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)



print(test_input1)
print(test_input2)

