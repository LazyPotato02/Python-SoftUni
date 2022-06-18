from os import PRIO_PGRP
import sys
from io import StringIO
test_input1 = '''14, 25, 37, 43, 19
58, 23, 37
'''
test_input2 = '''30, 13, 45
70, 25, 55, 15
'''
test_input3 = '''30, 25
20, 35
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

'''
if ramen == customer
    remove both 
    contineue with the next ramen and customer
if ramen > customer
    ramen -= customer
    remove customer
    try to match the same bow with new customer
if ramen < customer
    customer -= ramen
    remove bow
    try to match the same customer with new bow

last bow -- first customer
'''
from collections import deque

bows_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while customers and bows_of_ramen:
    ramen = bows_of_ramen.pop()
    customer = customers.popleft()
    if ramen == customer:
        pass
    if ramen > customer:
        ramen -= customer
        bows_of_ramen.append(ramen)
    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)

bows_of_ramen = [str(x) for x in bows_of_ramen]
customers = [str(x) for x in customers]
if not customers:
    print("Great job! You served all the customers.")
    if bows_of_ramen:
        print(f"Bowls of ramen left: {', '.join(bows_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(customers)}")
