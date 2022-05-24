n_and_m = input().split(' ')

n = int(n_and_m[0])
m = int(n_and_m[1])
n_set = set()
m_set = set()
for i in range(n):
    num = int(input())
    n_set.add(num)

for i in range(m):
    num = int(input())
    m_set.add(num)

final_set = set()
for i in n_set:
    if i in m_set:
        final_set.add(i)

print(*[x for x in final_set], sep='\n')
