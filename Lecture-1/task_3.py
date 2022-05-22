## List
# food_quantity = int(input())
# orders = input().split(' ')


# for i in range(0, len(orders)):
#     orders[i] = int(orders[i])
# print(max(orders))


# left_orders = []
# left = False
# for value in orders:
#     if (food_quantity - int(value)) > 0:
#         if not left:
#             food_quantity -= int(value)
#     else:
#         left = True
#     if left:
#         left_orders.append(str(value))

# if not left:
#     print('Orders complete')
# else:
#     print('Orders left: '+ ' '.join(left_orders) )

#Queue

from collections import deque

food = int(input())
order_queue = deque(map(int, list(input().split(' '))))
print(max(order_queue))

for _ in range(len(order_queue)):
    next_order = order_queue.popleft()
    if next_order > food:
        order_queue.appendleft(next_order)
        break
    else:
        food -= next_order

if len(order_queue) > 0:
    print(f"Orders left:", ' '.join(list(map(str, order_queue))))
else:
    print('Orders complete')