from collections import deque
import sys
from io import StringIO
test_input1 = '''20, 13, -7, 7
10, 5, 20, 15, 7, 9
'''
test_input2 = '''2, 4, 7, 8, 0
5, 6, 2
'''
test_input3 = '''12, 23
28, 40
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

from collections import deque


eggs = deque([int(x) for x in input().split(', ')])
paper_pieces = deque([int(x) for x in input().split(', ')])
# packaged_eggs = 0
boxes = 0
while eggs and paper_pieces:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    if egg == 13:
        paper_1 = paper_pieces.pop()
        paper_2 = paper_pieces.popleft()
        paper_pieces.appendleft(paper_1)
        paper_pieces.append(paper_2)
        continue

    paper = paper_pieces.pop()
    sum = egg + paper
    if sum <= 50:
        boxes += 1
        
if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if paper_pieces:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_pieces])}")