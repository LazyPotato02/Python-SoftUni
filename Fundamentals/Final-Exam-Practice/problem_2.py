import re

text = input()

reg = r'(@|#)([a-zA-Z]{3,})(\1\1)([a-zA-Z)]{3,})\1'
result = re.finditer(reg, text)


words = list()
for word in result:
    string = word.group(2,4)
    words.append(string)

reverse_words = list()


for word in words:
    to_reverse = word[1]
    reversed_word = to_reverse[::-1]
    main_string = word[0]
    if main_string == reversed_word:
        word = f"{main_string} <=> {word[1]}"
        reverse_words.append(word)


if len(words) == 0:
    print("No word pairs found!")
elif len(words) > 0:
    print(f"{len(words)} word pairs found!")

if len(reverse_words) > 0:
    print(f"The mirror words are:\n{', '.join(reverse_words)}")
else:
    print("No mirror words!")
