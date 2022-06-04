def register(name,license_plate,parking_dict):
    if name in parking_dict:
        print(f"ERROR: already registered with plate number {license_plate}")
    else:
        parking_dict[name] = license_plate
        print(f"{name} registered {license_plate} successfully" )
    return parking_dict

def unregister(name,license_plate,parking_dict):
    if name not in parking_dict:
        print(f"ERROR: user {name} not found")
    else:
        del parking_dict[name]
        print(f"{name} unregistered successfully")

def parking():
    parking_slots = int(input())
    parking_dict = {}

    for _ in range(parking_slots):

        command = input().split(' ')
        final_com = command[0]
        name = command[1]

        if len(command) == 3:
            license_plate = command[2]

        if final_com == 'register':
            register(name, license_plate, parking_dict)
        elif final_com == "unregister":
            unregister(name, license_plate, parking_dict)

    for k,v in parking_dict.items():
        print(f"{k} => {v}")

parking()