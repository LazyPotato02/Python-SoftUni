def create_matrix():
    matrix = []
    player = 1
    for row in range(6):
        ll = []
        for line in range(6):
            ll.append(0)

        matrix.append(ll)

    main(matrix, player)


def get_row(matrix, command, rows, player):
    matrix = matrix
    rows = rows
    command = command
    counter = 0

    try:
        while matrix[rows - counter][command] != 0:
            counter += 1
            if counter > 6:
                main(matrix, player)
            if matrix[rows - counter][command] == 0:
                matrix[rows - counter][command] = player + 1
                curr_row = rows - counter
                return matrix , curr_row
    except IndexError:
        return matrix



def is_win_condition(player, player_row, player_column, field):
    def normalize_player_position_in_direction(field, initial_row, initial_column, direction):
        row_delta, column_delta = direction

        row = initial_row
        column = initial_column
        row_delta *= -1
        column_delta *= -1
        rows_min_boundary = 0
        rows_max_boundary = len(field)
        columns_min_boundary = 0
        columns_max_boundary = len(field[0])

        while rows_min_boundary <= row < rows_max_boundary \
                and columns_min_boundary <= column < columns_max_boundary:
            if field[row][column] != player:
                break
            row += row_delta
            column += column_delta

        if row == initial_row and column == initial_column:
            return row, column

        return row - row_delta, column - column_delta

    def is_win_condition_in_direction(field, initial_row, initial_column, direction):
        row_delta, column_delta = direction
        row, column = normalize_player_position_in_direction(field, initial_row, initial_column, direction)
        rows_boundary = min(len(field), row + 4 * row_delta)
        columns_boundary = min(len(field[0]), column + 4 * column_delta)

        is_row_included = rows_boundary == row
        is_column_included = columns_boundary == column

        counter = 0
        while (row != rows_boundary or is_row_included) \
                and (column != columns_boundary or is_column_included) \
                and player == field[row][column]:
            counter += 1
            row += row_delta
            column += column_delta

        return counter == 4

    directions = [
        (0, 1),  # horizontal
        (1, 0),  # vertical
        (1, 1),  # main diagonal
        (-1, 1),  # secondary diagonal
    ]

    return any(is_win_condition_in_direction(field, player_row, player_column, direction) for direction in directions)

def print_winner(player):
    print(f'Player {player} wins!')



def main(matrix, player):
    matrix = matrix
    player = 1

    while True:
        rows = len(matrix) - 1
        starting_point = matrix[rows]


        if player % 2 == 0:  # Player 1
            player = 1
        else:
            player = 0  # Player 2

        if player == 0:
            print("Player 1, please chose a column")
            try:
                command = input()
                if command == 'Restart':
                    create_matrix()
                elif int(command) < len(matrix):
                    command = int(command) - 1
                else:
                    main(matrix, player)
            except ValueError:
                pass
        else:
            print("Player 2, please chose a column")
            try:
                command = input()
                if command == 'Restart':
                    create_matrix()
                elif int(command) < len(matrix):
                    command = int(command) - 1
            except ValueError:
                pass

        row = 5
        if starting_point[command] != 0:
            matrix, row = get_row(matrix, command, rows, player)
        else:
            starting_point[command] = player + 1

        if is_win_condition(player + 1, row, command, matrix):
            print_winner(player + 1)
            print("Do you wan't to restart? y/n")
            c = input()
            if c == 'y':
                create_matrix()
            else:
                break
                
        for i in range(len(matrix)):
            print(matrix[i])




if '__main__' == __name__:
    create_matrix()
