from collections import deque
import sys
from io import StringIO
test_input1 = '''4 5 7 3 6 9 12
12 9 6 1
'''.strip()
test_input2 = '''3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4
'''
test_input3 = '''200
5 15 32 20 10 5
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

from collections import deque


males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0
while males and females:

    male = males.pop()
    if male % 25 == 0 or male <= 0:
        if male % 25 == 0 and male != 0 and males:
            males.pop()
        continue
        
    female = females.popleft()
    if female % 25 == 0 or female <= 0:
        if female % 25 == 0 and female != 0 and females:
            females.popleft()
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        males.append(male -2)


print(f"Matches: {matches}")
if males:
    print("Males left: ", ', '.join(reversed([str(x) for x in males])), sep='')
else:
    print('Males left: none')
if females:
    print("Females left: ", ', '.join([str(x) for x in females]), sep='')
else:
    print('Females left: none')