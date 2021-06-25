COMANDS = ["up", "down", "left", "right"]
WALL = "X"


def read_matrix(n):
    matrix = []
    player_row_index = None
    player_col_index = None

    for row in range(n):
        data_for_each_row = list(input().split())
        current_row = []
        if "P" in data_for_each_row:
            player_row_index = row
            player_col_index = data_for_each_row.index("P")
        for el in data_for_each_row:
            if el.isdigit():
                current_row.append(int(el))
            else:
                current_row.append(el)

        matrix.append(current_row)

    return (matrix, player_row_index, player_col_index)


def get_next_move(row, col, dir):
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return row + row_delta, col + column_delta


def is_index_valid(row_value, row_max_value, col_value, col_max_value):
    if 0 <= row_value < row_max_value \
            and 0 <= col_value < col_max_value \
            and not matrix[row_value][col_value] == WALL:
        return True
    return False


number = int(input())
matrix, player_row_index, player_col_index = read_matrix(number)
coins = 0
path = []
has_won = False

while True:
    if coins >= 100:
        has_won = True
        break
    command = input()
    if command in COMANDS:
        next_row_index, next_col_index = get_next_move(player_row_index, player_col_index, command)
        if is_index_valid(next_row_index, len(matrix), next_col_index, len(matrix[0])):
            coins += matrix[next_row_index][next_col_index]
            player_row_index = next_row_index
            player_col_index = next_col_index
            coins_collected_position = [player_row_index, player_col_index]
            path.append(coins_collected_position)

        else:
            coins = coins // 2
            break

if has_won:
    print(f"You won! You've collected {coins} coins.")
    print(f"Your path:")
    for [row, col] in path:
        print([row, col])

else:
    print(f"Game over! You've collected {coins} coins.")
    print(f"Your path:")
    for [row, col] in path:
        print([row, col])
