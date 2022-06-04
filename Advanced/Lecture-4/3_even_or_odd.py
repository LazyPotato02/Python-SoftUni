def even_odd(*args):
    param = args[-1]
    numbers = list()
    for v in args[:-1]:
        if param == 'even':
            if v % 2 == 0:
                numbers.append(v)
        else:
            if v % 2 != 0:
                numbers.append(v)
    
    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
