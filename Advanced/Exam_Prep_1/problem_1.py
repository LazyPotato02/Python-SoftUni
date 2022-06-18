import sys
from io import StringIO
test_input1 = '''10 16 13 25
12 11 8
'''
test_input2 = '''10 14 22 4 5
11 16 17 11 1 8
'''
test_input3 = '''5 6 7
2 1 5 7 5 3
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

from collections import deque

elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]
turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spent += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factory)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)


print(f'Toys: {toys_count}')
print(f'Energy: {total_energy_spent}')
if elf_energies:
    elves_string = ', '.join(str(x) for x in elf_energies)
    print(f'Elves left: {elves_string}')
if boxes:
    boxes_string = ', '.join(str(x) for x in boxes)
    print(f'Boxes left: {boxes_string}')