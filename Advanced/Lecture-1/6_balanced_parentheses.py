my_stack = []
balanced = True
bundle = {'(':')','{':'}','[':']'}
input_line = input()

for x in input_line:
    if x in bundle.keys():
        my_stack.append(x)
    elif my_stack and x == bundle.get(my_stack.pop()):
        continue
    else:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')
    