element_count = int(input())

elements = set()

for _ in range(element_count):
    chemical_element = input().split(' ')
    for element in chemical_element:
        elements.add(element)

print(*[x for x in elements], sep='\n')
