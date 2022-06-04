
def office_manager(number_of_rooms):
    left_chairs = 0
    is_room_free = True
    
    for room_number in range(number_of_rooms + 1):
        data = input().split(' ')
        available_chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(available_chairs) - visitors)

        if len(available_chairs) < visitors:
            is_room_free = False
            print(f"{diff} more chairs needed in room {room_number}")
        elif len(available_chairs) > visitors:
            left_chairs += dict

    if is_room_free:
        print(f'Game on, {left_chairs} free chairs left')


halls = int(input())
office_manager(halls)