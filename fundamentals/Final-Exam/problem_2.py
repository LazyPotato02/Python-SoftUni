import re

iters = int(input())

reg = r'(\|)([A-Za-z]{4,})(\1)(:)#([A-Za-z]*) ([A-Za-z]*)#'

result = ''
for _ in range(iters):
    strg = input()
    result = re.finditer(reg, strg)
    res = ''
    for res in result:
        name = res.group(2)
        job = res.group(5) + ' ' + res.group(6)
        print(f"{name}, The {job}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(job)}")
    if not res:
        print("Access denied!")
