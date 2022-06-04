input_string = input()

word_list = []
unique_chars = set()
index = 0

while index < len(input_string):
    if input_string[index].isnumeric():
        word = input_string[:index].upper()
        for ch in word:
            unique_chars.add(ch)

        i = index
        while input_string[i].isnumeric(): 
            i += 1
            if i == len(input_string):
                break
        count = int(input_string[index:i])
        word_list.append((word,count))
        input_string = input_string[i:]   
        index = 0
    else:
        index += 1
else:
    print(f'Unique symbols used: {len(unique_chars)}')
    for word in word_list:
        print(word[0] * word [1], end='')