# import sys
# from io import StringIO
# test_input1 = '''1 2 3 |4 5 6 |  7  88
# '''


# sys.stdin = StringIO(test_input1)
#----------------------------------------------------------------------------------------#
            #Method #1
input_line = input()
while "  " in input_line:
    input_line = input_line.replace('  ', ' ')
else:
    data = [x for x in reversed([y.strip() for y in input_line.split('|')]) if x != '']
    print(' '.join(data).strip())

#----------------------------------------------------------------------------------------#
            #Method #2
input_line = input().split("|")
result = []

for idx in range(len(input_line) -1, -1 , -1):
    result.append(input_line[idx].strip().split())

final_res = []

for i in range(len(result)):
    for z in result[i]:
        final_res.append(z)
    
print(' '.join(final_res))

#----------------------------------------------------------------------------------------#
            #Method #3

input_line = input().split("|")
result = []

for idx in range(len(input_line) -1, -1 , -1):
    result.extend(input_line[idx].strip().split())

print(' '.join(result))
