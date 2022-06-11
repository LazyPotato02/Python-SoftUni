#==Global Variables==#

#==If game is still going==#
game_still_going = True

#==Winner==#
winner = None

#Turns
current_player = "X"

#==Board==#
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Start the game of tic_tac_toe
def play_game():

    #==Board display==#
    display_board()
    #While the game is still going
    while game_still_going:
        #Handle single turn
        handle_turn(current_player)
        #Check if game ended
        check_if_game_over()
        #Flip to other player
        flip_player()


    #Game ending
    if winner == "X" or winner == "O":
        print("The winner is " + winner)
    elif winner == None:
        print("Tie.")


#Handle single turn function
def handle_turn(player):
    print(player + " s turn.")

    position = input("Chose a position from 1-9: ")
    valid = False
    while not valid:


        while position not in ["1", "2", "3","4","5","6","7","8","9"]:
            position = input("Invalid input. Chose a position from 1-9: ")


        position = int(position) - 1

        if board[position] == "-":
            valid = True
            print("You can't go there! Try again?")

    board[position] = player

    display_board()

#Checks game state
def check_if_game_over():
    check_if_win()
    check_if_tie()


#Check the winner
def check_if_win():

    global winner

    #==check rows==#
    row_winner = check_rows()
    #==check columns==#
    column_winner = check_columns()
    #==check diagonals==#
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return



def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]    

    return

def check_columns():
    global game_still_going

    columnd_1 = board[0] == board[3] == board[6] != "-"
    columnd_2 = board[1] == board[4] == board[7] != "-"
    columnd_3 = board[2] == board[5] == board[8] != "-"
    if columnd_1 or columnd_2 or columnd_3:
        game_still_going = False
    if columnd_1:
        return board[0]
    elif columnd_2:
        return board[1]
    elif columnd_3:
        return board[2]    


    return

def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]


    return



#Check if tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return

play_game()