replace_symbols = ["-", ",", ".", "!", "?"]
file = open("./test_1.txt", 'r')

string_f = []

for row in file.readlines():
    x = row.strip()
    for replace in replace_symbols:
        x = x.replace(replace, '@')
    string_f.append(x)

final = []

for x in string_f:
    reversed_str = []
    rever = x.split()
    for i in range(len(rever)):
        reversed_str.append(rever[i])

    final.append(reversed_str)
    print(" ".join(reversed_str[::-1]))
