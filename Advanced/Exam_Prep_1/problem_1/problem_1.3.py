import sys
from io import StringIO
test_input1 = '''105 20 30 25
120 60 11 400 10 1
'''
test_input2 = '''30 5 21 6 0 91
15 9 5 15 8
'''
test_input3 = '''200
5 15 32 20 10 5
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

'''
if result is between or equal to the needed_magic:
    make gift
    remove magic_value and materials

Otherwise:
    if the product is under 100:
        if is even:
            double the materials and triple the magic 
            sum them
        if is odd:
            double the sum of both
            check again: check if it is between or equal to the needed power
    if the product is more than 499:
        devide by 2
        check if it is between or equal to the needed power
    if not between:
        remove both material and magic level

Stop crafting when no materials or magic level

Pairs to succeed:
    gemstone - sculpture
    gold - jewellery
'''
from collections import deque


gifts = {
    1: 'Gemstone',
    2: 'Porcelain Sculpture',
    3: 'Gold',
    4: 'Diamond Jewellery'
}
materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])
presents = []

while materials and magic_levels:
    material = materials.pop()
    level = magic_levels.popleft()
    mix = material + level

    if mix < 100:
        if mix % 2 == 0:
            mix = material * 2 + level * 3
        else:
            mix *= 2

    elif mix > 499:
        mix /= 2

    gift = gifts.get(mix//100)
    if gift:
        presents.append(gift)

if gifts.get(1) in presents and gifts.get(2) in presents:
    print('The wedding presents are made!')
elif gifts.get(3) in presents and gifts.get(4) in presents:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left:', ', '.join([str(el) for el in materials]))
if magic_levels:
    print(f'Magic left:', ', '.join([str(el) for el in magic_levels]))

sorted_list = sorted([(el, presents.count(el)) for el in set(presents)])
for item in sorted_list:
    print(f'{item[0]}: {item[1]}')