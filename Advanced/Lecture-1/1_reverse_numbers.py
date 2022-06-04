num_to_reverse = input().split(' ')
reversed_stack = []

for n in range(len(num_to_reverse)):
    reverse = num_to_reverse.pop()
    reversed_stack.append(reverse)

print(' '.join(reversed_stack))
