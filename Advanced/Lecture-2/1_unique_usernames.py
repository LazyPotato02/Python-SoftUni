sequence_count = int(input())

unique_names = set()

for _ in range(sequence_count):
    name = input()
    unique_names.add(name)

print(*[x for x in unique_names], sep='\n')
