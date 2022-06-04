c1, c2 = input(), input()


def char_range(c1, c2):
    for c in range(ord(c1) + 1, ord(c2)):
        yield chr(c)

for c in char_range(c1, c2):
    print(c, end=" ")