spell = input()
command = input().split(' ')

while command[0] != 'Abracadabra':
    
    if command[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command[0] == 'Illusion':
        index = int(command[1])
        letter = command[2]

        if index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print('Done!')
        else:
            print('The spell was too weak.')
    elif command[0] == 'Divination':
        first_substr = command[1]
        second_substr = command[2]

        if first_substr in spell:
            spell = spell.replace(first_substr, second_substr)
            print(spell)

    elif command[0] == 'Alteration':
        substr = str(command[1])

        if substr in spell:
            spell = spell.replace(substr,'')
            print(spell)
    else:
        print('The spell did not work!')


    command = input().split(' ')

