import sys
a, b, c = int(input()), int(input()), int(input())
def smallest(a,b,c):
    new_list = [a,b,c]
    max_number = -sys.maxsize
    min_number = sys.maxsize
    for i in new_list:
        if i <= min_number:
            min_number = i
        elif i >= max_number:
            max_number = 1
    print(min_number)

smallest(a,b,c)