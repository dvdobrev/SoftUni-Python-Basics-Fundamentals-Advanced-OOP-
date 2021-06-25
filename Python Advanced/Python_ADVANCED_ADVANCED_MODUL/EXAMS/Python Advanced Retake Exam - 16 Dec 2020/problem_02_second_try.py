PLAYER = "P"
EMPTY = "-"

text = input()
number = int(input())


def read_matrix(n):
    matrix = []
    player_row_index = None
    player_col_index = None

    for row in range(n):
        current_row = list(input())
        if "P" in current_row:
            player_row_index = row
            player_col_index = current_row.index("P")

        matrix.append(current_row)

    return (matrix, player_row_index, player_col_index)


def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value


def get_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return row + row_delta, col + column_delta


matrix, player_row_index, player_col_index = read_matrix(number)

moves_count = int(input())
for m in range(moves_count):
    move = input()
    next_row_index, next_col_index = get_next_move(player_row_index, player_col_index, move)
    if is_index_valid(next_row_index, len(matrix)) and is_index_valid(next_col_index, len(matrix[0])):
        symbol = matrix[next_row_index][next_col_index]
        if symbol.isalpha():
            text += symbol
            matrix[player_row_index][player_col_index] = EMPTY
            matrix[next_row_index][next_col_index] = PLAYER
            player_row_index = next_row_index
            player_col_index = next_col_index

        else:
            matrix[player_row_index][player_col_index] = EMPTY
            matrix[next_row_index][next_col_index] = PLAYER
            player_row_index = next_row_index
            player_col_index = next_col_index

    else:
        if text:
            text = text[:-1]

print(text)
# print(*matrix, sep="\n")
for el in matrix:
    print("".join(el))
# print(*["".join(el) for el in matrix])
