loops = int(input())
stack_querie = []

for _ in range(loops):
    n = input()
    if n[0] == '1':
        stack_querie.append(n[2:])
    elif stack_querie:
        if n == '2':
            stack_querie.pop()
        elif n == '3':
            print(max(stack_querie))
        elif n == '4':
            print(min(stack_querie))

final_stack = []
for n in range(len(stack_querie)):
    popped = stack_querie.pop()
    final_stack.append(popped)

print(', '.join(final_stack))
