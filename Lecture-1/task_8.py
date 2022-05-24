from collections import deque


def queue_len(lst:list) -> int:
    if lst:
        return sum([len(x) for x in lst])
    else:
        return 0

road_queue = deque()
crossroad = deque()
entry_window = int(input())
exit_window = int(input())
passed_cars = 0
crash_char = ''

while True:
    input_line = input()
    if input_line == 'END':
        break

    if input_line == 'green':
        time_to_enter = entry_window
        while road_queue and time_to_enter > 0:
            entering_car = road_queue.popleft()
            crossroad.append(entering_car)
            time_to_enter -= len(entering_car)
        
        time_left = entry_window + exit_window
        while crossroad:
            car = crossroad.popleft()
            if len(car) <= time_left:
                time_left -= len(car)
                passed_cars += 1
                continue
            else:
                crash_char = car[time_left]
                break

        if crash_char:
            print("A crash happened!")
            print(f"{car} was hit at {crash_char}.")
            break

    else:
        road_queue.append(input_line)
    
if not crash_char:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")