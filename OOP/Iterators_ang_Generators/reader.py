def read_next(*args):
    for arg in args:
        for el in arg:
            yield el



for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)