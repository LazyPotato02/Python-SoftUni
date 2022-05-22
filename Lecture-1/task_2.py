import sys


loops = int(input())

stack_querie = []

for _ in range(loops):

    n = input().split(' ')

    index = int(n[0])
    if index == 1:
        num_to_add = n[1]
        stack_querie.append(num_to_add)
    elif index == 2:
        if len(stack_querie) > 0:
            stack_querie.pop()
    elif index == 3:
        print(max(stack_querie))
    elif index == 4:
        min_num = int(sys.maxsize)
        for i in range(len(stack_querie)):
            if int(stack_querie[i]) < min_num:
                print(min_num)
        # print(min(stack_querie))


final_stack = []
for n in range(len(stack_querie)):
    popped = stack_querie.pop()
    final_stack.append(popped)

print(', '.join(final_stack))