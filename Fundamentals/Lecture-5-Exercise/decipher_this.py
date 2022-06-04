import re

words = input().split(' ')
word_list = []
for word in words:
    res = re.split("(\d+)", word)
    number = chr(int(res[1]))
    strings = res[2]
    if len(strings) <= 1:
        word_list.append(f"{number}{strings[-1]}{strings[1:(len(strings)- 1)]}")
    else:
        word_list.append(f"{number}{strings[-1]}{strings[1:(len(strings)- 1)]}{strings[0]}")

print(' '.join(word_list))