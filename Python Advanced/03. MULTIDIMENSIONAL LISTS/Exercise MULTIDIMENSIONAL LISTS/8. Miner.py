def read_matrix(size):
    matrix = []

    for row in range(size):
        line = input().split()
        sub_matrix = [line[el] for el in range(len(line))]
        matrix.append(sub_matrix)

    return matrix


def find_the_start(matrix):  # Find the thing we are searching for
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == "s":
                return (y, x)


def find_all_coals(matrix):
    coals_position = []
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            current_position = []
            if char == "c":
                current_position.append(y)
                current_position.append(x)
                coals_position.append(current_position)

    return coals_position


def get_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return (row + row_delta, col + column_delta)


size = int(input())
directions = [el for el in input().split()]
matrix = read_matrix(size)
row_index, col_index = find_the_start(matrix)
coals_position = find_all_coals(matrix)
total_coals = len(coals_position)
collected_coals = 0
is_all_collected_or_end = False

for direction in directions:
    if not is_all_collected_or_end:  # not all is collected
        next_row_index, next_col_index = get_next_move(row_index, col_index, direction)
        if 0 <= next_row_index < size and 0 <= next_col_index < size:
            symbol = matrix[next_row_index][next_col_index]
            if symbol == "*":
                matrix[next_row_index][next_col_index] = "s"
                matrix[row_index][col_index] = "*"
                row_index, col_index = next_row_index, next_col_index
            elif symbol == "e":
                print(f"Game over! ({next_row_index}, {next_col_index})")
                is_all_collected_or_end = True
                break
            elif symbol == "c":
                collected_coals += 1
                matrix[next_row_index][next_col_index] = "s"
                matrix[row_index][col_index] = "*"
                row_index, col_index = next_row_index, next_col_index
                if total_coals == collected_coals:
                    is_all_collected_or_end = True
                    print(f"You collected all coals! ({next_row_index}, {next_col_index})")
                    break

    else:   # all is collected or hit the end
        break
        
if not is_all_collected_or_end:
    print(f"{total_coals - collected_coals} coals left. ({row_index}, {col_index})")