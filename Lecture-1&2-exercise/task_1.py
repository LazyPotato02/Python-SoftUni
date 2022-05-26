first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command_part = input().split()
    command = command_part[0]
    target_set = command_part[1]


    if command == 'Add':
        if target_set == 'First':
            first = first.union([int(x) for x in command_part[2:]])
        else:
            second = second.union([int(x) for x in command_part[2:]])
    elif command == 'Remove':
        if target_set == 'First':
            first = first.difference([int(x) for x in command_part[2:]])
        else:
            second = second.difference([int(x) for x in command_part[2:]])
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
