import sys
from io import StringIO
test_input1 = '''11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1
'''.strip()
test_input2 = '''10, 9, 8, 7, 5
5, 10, 9, 8, 7
'''.strip()
test_input3 = '''12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1
'''.strip()
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees_pizza_cap = [int(x) for x in input().split(', ')]
total_pizzas = 0

while pizza_orders and employees_pizza_cap:

    order = pizza_orders.popleft()
    if 0 < order <= 10 :
        employee = employees_pizza_cap.pop()
        if order <= employee:
            total_pizzas += order
        elif order > employee:
            total_pizzas += employee
            order -= employee 
            pizza_orders.appendleft(order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees_pizza_cap])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")