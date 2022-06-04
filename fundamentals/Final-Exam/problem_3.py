
words = input().split(" | ")

notebook = dict()
teacher_words = list()
while words[0] != 'Test' and words[0] != 'Hand Over':
    for word in words:
        splited = word.split(": ")

        if len(splited) > 1:

            if splited[0] in notebook:
                notebook[splited[0]].append(splited[1])
            else:
                notebook[splited[0]] = [splited[1]]
        else:
            teacher_words = [word for word in words]
        

    words = input().split(" | ")


if words[0] == 'Hand Over':
    for k,v in notebook.items():
        print(k, end=' ')
elif words[0] == 'Test':

    for t_word in teacher_words:
        if t_word in notebook:
            needed_words = list()
            k = notebook.get(t_word)

            print(f"{t_word}:")
            for wor in k:
                print(f" -{wor}")
