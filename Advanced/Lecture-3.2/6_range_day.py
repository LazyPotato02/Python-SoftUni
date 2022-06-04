move = {
    'up': lambda cell, steps: (cell[0] - steps, cell[1]),
    'down': lambda cell, steps: (cell[0] + steps, cell[1]),
    'left': lambda cell, steps: (cell[0], cell[1] - steps),
    'right': lambda cell, steps: (cell[0], cell[1] + steps)
}


def move_a_cell(matrix: list, cell: tuple, direction: str, steps: int) -> tuple:
    """ Move the shooter cell. If new cell is out of range returns the current cell """

    new_cell = move[direction](cell, int(steps))
    if cell_valid(new_cell):
        if get_value(matrix, new_cell) in ('.', 'A'):
            return new_cell
    return cell


def cell_valid(cell: tuple) -> bool:
    """ Validates if cell is out of range"""
    if 0 <= min(cell) and max(cell) < 5:
        return True
    else:
        return False


def shoot(matrix: list, cell: tuple, direction: str) -> tuple:
    """ Finds an 'x' cell in the firing direction. \
        Returns none if no targets in that direction"""
    target_cell = move[direction](cell, 1)
    while cell_valid(target_cell):
        if get_value(matrix, target_cell) == 'x':
            return target_cell
        target_cell = move[direction](target_cell, 1)


def get_value(matrix: list, cell: tuple) -> str:
    """ Gets the value at the x,y coordinates in the matrix"""
    row, col = cell
    return str(matrix[row][col])


def set_value(matrix: list, cell: tuple, value: str) -> list:
    """ Changes the value at the x, y coordinates in the matrix """
    row, col = cell
    matrix[row][col] = value
    return matrix


def main() -> None:

    matrix = []
    shot_targets = []
    starting_targets = 0
    a_cell = None

    for i in range(5):
        row = [el for el in input().split()]
        matrix.append(row)
        starting_targets += row.count('x')
        if 'A' in row:
            a_cell = (i, row.index('A'))

    for _ in range(int(input())):
        input_line = input().split()

        command, direction = input_line[0], input_line[1]
        
        if command == 'move':
            steps = int(input_line[2])
            a_cell = move_a_cell(matrix, a_cell, direction, steps)

        elif command == 'shoot':
            hit_target = shoot(matrix, a_cell, direction)
            if hit_target:
                matrix = set_value(matrix, hit_target, '.')
                shot_targets.append(list(hit_target))

        if len(shot_targets) == starting_targets:
            break

    if len(shot_targets) == starting_targets:
        print(f'Training completed! All {starting_targets} targets hit.')

    else:
        print(f'Training not completed! {starting_targets-len(shot_targets)} targets left.')

    if shot_targets:
        print(*shot_targets, sep='\n')


if __name__ == '__main__':
    main()