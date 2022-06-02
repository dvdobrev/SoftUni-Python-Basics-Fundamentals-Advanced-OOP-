EMPTY_SPACE = "."
PLAYER = "A"
TARGET = "x"


def read_matrix(n):
    matrix = []
    player_row_index = None
    player_col_index = None
    targets_count = 0

    for row in range(n):
        current_row = list(input().split())
        if "A" in current_row:
            player_row_index = row
            player_col_index = current_row.index("A")

        for el in current_row:
            if el == "x":
                targets_count += 1

        matrix.append(current_row)

    return (matrix, player_row_index, player_col_index, targets_count)


def get_next_move(row, col, dir, steps):
    dir_deltas = {
        "up": (-steps, 0),
        "down": (+steps, 0),
        "left": (0, -steps),
        "right": (0, + steps),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return row + row_delta, col + column_delta


def shot_next_target(row, col, dir):
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]
    row += row_delta
    col += column_delta

    return row, col


def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value


matrix, player_row_index, player_col_index, targets_count = read_matrix(5)
shooted_target = 0
# print(*matrix, sep="\n")

commans_number = int(input())
shot_targets = []
has_shot_a_target = False

for i in range(commans_number):
    command, direction, *args = input().split()
    if command == "move":
        steps = int(args[0])
        next_row_index, next_col_index = get_next_move(player_row_index, player_col_index, direction, steps)
        if is_index_valid(next_row_index, len(matrix)) and is_index_valid(next_col_index, len(matrix[0])):
            if matrix[next_row_index][next_col_index] == EMPTY_SPACE:
                matrix[player_row_index][player_col_index] = EMPTY_SPACE
                player_row_index = next_row_index
                player_col_index = next_col_index
                matrix[player_row_index][player_col_index] = PLAYER

    elif command == "shoot":
        target_row_index, target_col_index = shot_next_target(player_row_index, player_col_index, direction)
        while True:

            if is_index_valid(target_row_index, len(matrix)) and is_index_valid(target_col_index,
                                                                                len(matrix[0])):
                if not matrix[target_row_index][target_col_index] == TARGET:
                    target_row_index, target_col_index = shot_next_target(target_row_index, target_col_index, direction)

                else:
                    shooted_target += 1
                    shot_targets.append([target_row_index, target_col_index])
                    matrix[target_row_index][target_col_index] = EMPTY_SPACE
            else:
                break

        # print()
        # print(*matrix, sep="\n")

if shooted_target == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")

else:
    print(f"Training not completed! {targets_count - shooted_target} targets left.")

for el in shot_targets:
    print(el)
