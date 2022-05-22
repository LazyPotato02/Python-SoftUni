from collections import deque

def circle(pump_d) -> bool:
    fuel = 0
    for i in range(len(pump_d)):
        ltr, km = pump_d[i]
        fuel += ltr - km
        if fuel < 0:
            return False
    return True


pumps_in_circle = int(input())
fuel_pumps = deque()

for _ in range(pumps_in_circle):
    data = tuple(map(int, input().split()))
    fuel_pumps.append(data)

for i in range(len(fuel_pumps)):
    if circle(tuple(fuel_pumps)):
        break
    fuel_pumps.rotate(-1)
print(i)
