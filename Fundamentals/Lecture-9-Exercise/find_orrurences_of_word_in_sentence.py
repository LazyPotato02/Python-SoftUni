import re

sentence = input()
word = input()

regex = rf"\b{word}\b"
result = re.findall(regex, sentence, re.IGNORECASE)
print(len(result))

