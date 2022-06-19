import sys
from io import StringIO
test_input1 = '''o e a o e a i
p r s x r
'''
test_input2 = '''a a a
x r l t p p
'''
test_input3 = '''u a o i u y o e
p m t l
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

from collections import deque

rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}


vowels = deque(input().split())
consonants = input().split()
found_letters = set()
is_found = False
while vowels and consonants:

    vowel = vowels.popleft()
    consonant = consonants.pop()

    if vowel in rose:
        rose[vowel] = True
    if consonant in rose:
        rose[consonant] = True
    if all(rose.values()):
        print("Word found: rose")
        is_found = True
        break
    if vowel in tulip:
        tulip[vowel] = True
    if consonant in tulip:
        tulip[consonant] = True
    if all(tulip.values()):
        print(" Word found: tulip")
        is_found = True
        break
    if vowel in lotus:
        lotus[vowel] = True
    if consonant in lotus:
        lotus[consonant] = True
    if all(lotus.values()):
        print(" Word found: lotus")
        is_found = True
        break
    if vowel in daffodil:
        daffodil[vowel] = True
    if consonant in daffodil:
        daffodil[consonant] = True
    if all(daffodil.values()):
        print(" Word found: daffodil")
        is_found = True
        break


if not is_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
