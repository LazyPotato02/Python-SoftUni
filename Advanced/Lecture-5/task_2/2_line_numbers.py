from curses.ascii import isalpha


file = open("./test_2.txt", 'r')

count = 0
for line in file.readlines():
    count += 1
    punc_count = 0
    original = line
    line = line.strip()
    line = line.replace(" ", "")
    for al in line:
        if not isalpha(al):
            punc_count += 1
    al_count = len(line) - punc_count

    f = open("./output.txt", 'a')
    f.write(f"Line {count}: {original} ({al_count})({punc_count}) \n")
    f.close()
