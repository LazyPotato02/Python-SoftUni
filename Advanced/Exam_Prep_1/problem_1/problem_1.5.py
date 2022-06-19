import sys
from io import StringIO
test_input1 = '''5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
'''
test_input2 = '''-15, -8, 0, -16, 0, -22
10, 5
'''
test_input3 = '''200
5 15 32 20 10 5
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)
'''
Start from the first effect and try to mix it with the last explosive power

if sum of both::
    if divisible by 3 but not divisible by 5:
        create palm firework and remove both the effect and power
    if divisible by 5 but not divisible by 3:
        create willow firework and remove both the effect and power
    else:
        divisible by 3 and 5 create crossette firework and remove both the effect and power
else:
    decrease value of firework_effect by 1 and move to the end
    then try to mix the next firework_effect with the same explosive power
if value is below or equal to 0 remove it from the sentance before trying to mix it with the others

to make perfect show Maria needs 3 of each ot the firework types

'''

from collections import deque

firework_effect = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

def done():
    return palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3

while firework_effect and explosive_power and not done():

    firework = firework_effect.popleft()

    if firework <= 0 :
        continue

    expl_power = explosive_power.pop()


    if expl_power <= 0:
        firework_effect.appendleft(firework)
        continue
    
    mix = firework + expl_power
    

    if mix % 3 == 0 and not mix % 5 == 0:
        palm_firework += 1
    elif mix % 5 == 0 and not mix % 3 == 0:
        willow_firework += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        crossette_firework += 1
    else:
        firework -= 1
        firework_effect.append(firework)
        explosive_power.append(expl_power)



if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effect])}")
if explosive_power:
    print(f" Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")