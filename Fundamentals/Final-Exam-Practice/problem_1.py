def secret_chat(data):

    command = input().split(":|:")

    while True:

        if command[0] == "Reveal":
            print(f"You have a new text message: {''.join(data)}")
            break
        elif command[0] == "InsertSpace":
            index = int(command[1])
            data = data[:index] + " " + data[index:]
            print(data)
        elif command[0] == "Reverse":
            substring = command[1]
            if substring in data:
                start_index = data.index(substring)
                end_index = start_index + len(substring)
                data = data[:start_index] + data[end_index:] + substring[::-1]
                print(data)
            else:
                print("error")
        elif command[0] == "ChangeAll":
            orig_word = command[1]
            replace_word = command[2]

            data = data.replace(orig_word, replace_word)
            print(data)

        
        command = input().split(":|:")

data = input()
secret_chat(data)

