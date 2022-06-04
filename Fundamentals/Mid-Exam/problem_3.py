sequence = input().split(', ')
command_inp = input().split(" - ")

while command_inp[0] != "End":

    command = command_inp[0]
    value = command_inp[1]

    if command == "Add":
        if value in sequence:
            pass
        else:
            sequence.append(value)
    elif command == "Remove":
        if value in sequence:
            sequence.remove(value)
    elif command == "Bonus phone":
        splitted = value.split(":")
        old_phone = splitted[0]
        new_phone = splitted[1]
        if old_phone in sequence:
            index = sequence.index(old_phone)
            sequence.insert(index + 1, new_phone)
    elif command == "Last":
        if value in sequence:
            sequence.remove(value)
            sequence.append(value)


    command_inp = input().split(" - ")


print(", ".join(sequence))