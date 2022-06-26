from collections import deque
import sys
from io import StringIO
test_input1 = '''Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)
'''
test_input2 = '''Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)
'''
test_input3 = '''Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

from collections import deque

first_player, second_player = input().split(', ')

ROWS_COUNT = 6
COLS_COUNT = 6

matrix = [input().split() for _ in range(ROWS_COUNT)]
is_hit = False
skip = deque()

while True:

    player = first_player



    player_pos = ''
    try:
        player_pos = tuple(map(int, input().replace(
            '(', '').replace(')', '').split(', ')))
    except EOFError:
        break
    row, col = player_pos

    if skip:
        skip_ = skip.popleft()
    
        if skip_ == player:
            first_player, second_player = second_player, first_player
            continue
        else:
            skip.appendleft(skip_)

    if matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {second_player}.")
        break
    elif matrix[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        skip.append(player)

    first_player, second_player = second_player, first_player
