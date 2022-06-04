win_symbols = ('@', '#', '$', '^')
win_patterns = [x * 6 for x in win_symbols]
find_pattern = lambda x: next(filter(lambda y: y in x,win_patterns),None)

tickets_list = input().split(',')
tickets_list = [ticket.strip() for ticket in tickets_list if ticket.strip() != '']

for ticket in tickets_list:
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        pattern_found = find_pattern(ticket[:10])      
        if pattern_found and (pattern_found in ticket[10:]): #winning ticket 
            pattern_char = pattern_found[0]

            if ticket == pattern_char * 20: #Jacpot ticket
                print(f'ticket "{ticket}" - 10{pattern_char} Jackpot!')
            
            else: #regular winnig ticket
                for i in range(10,5,-1):
                    if (pattern_char * i in ticket[:10]) and (pattern_char * i in ticket[10:]):
                        print(f'ticket "{ticket}" - {i}{pattern_char}')
                        break
        else: #valid but not winning
            print(f'ticket "{ticket}" - no match')