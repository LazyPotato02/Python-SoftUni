import re


while True:
    text = input()
    
    if not text:
        break

    exp = re.findall(r"\d+",text)

    if len(exp) > 0:
        print(' '.join(exp), end=' ')