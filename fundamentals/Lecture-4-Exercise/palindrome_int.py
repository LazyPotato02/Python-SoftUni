a = list(map(int,input().split(", ")))

for i in a:
    res = str(i) == str(i)[::-1]
    print(str(res))