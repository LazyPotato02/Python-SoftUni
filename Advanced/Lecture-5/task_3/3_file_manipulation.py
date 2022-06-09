from genericpath import exists
from os import remove


while True:

    command = input()

    if command == 'End':
        break

    parameters = command.split("-")

    if parameters[0] == "Create":
        file = "./"+str(parameters[1])
        with open(file, 'w') as f:
            pass
    elif parameters[0] == "Add":
        file = "./"+str(parameters[1])
        text = str(parameters[2])
        with open(file, 'a') as f:
            f.write(text + "\n")
    elif parameters[0] == "Replace":
        try:
            file = "./"+str(parameters[1])
            text = str(parameters[2])
            replace = str(parameters[3])
            filedata = ''
            with open(file, 'r') as file_1:
                filedata = file_1.read()
            filedata = str(filedata.replace(text, replace))
            with open(file, 'w') as file_2:
                file_2.write(filedata)
        except Exception:
            print("An error occurred")
    elif parameters[0] == "Delete":
        file = "./"+str(parameters[1])
        if not exists(file):
            print("An error occurred")
            continue

        remove(file)
