sequence = list(map(int,input().split(' ')))
command_inp = input().split(" ")

while command_inp[0] != "Finish":

    command = command_inp[0]
    value = int(command_inp[1])
    replace_value = " "

    if len(command_inp) == 3:
        replace_value = int(command_inp[2])

    if command == "Add":
        sequence.append(value)
    elif command == "Remove":
        sequence.remove(value)
    elif command == "Replace":
        if value in sequence:
            index = sequence.index(value)
            sequence.pop(index)
            sequence.insert(index, replace_value)
    elif command == "Collapse":
        result = [res for res in sequence if value <= int(res)]
        sequence = result


    command_inp = input().split(" ")

sequence = list(map(str,sequence))
print(" ".join(sequence))