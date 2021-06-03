PLAYER = "P"
WALL = "X"
COMMANDS = ["up", "down", "left", "right"]


def read_matrix():
    matrix = []

    for row in range(n):
        line = input().split()
        sub_matrix = []
        for col in line:
            if col.isnumeric():
                sub_matrix.append(int(col))
            else:
                sub_matrix.append(col)
        matrix.append(sub_matrix)


    return matrix


def find_the_player(matrix): # Find the thing we search
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if PLAYER == char:
                return (y, x)



def get_next_move(position, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_index, column_index) = player_position
    (row_delta, column_delta) = dir_deltas[dir]

    return row_index + row_delta, column_index + column_delta


def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value


n = int(input())
matrix = read_matrix()
player_position = find_the_player(matrix)
total_coins = 0
path = []

while True:
    command = input()
    if command in COMMANDS:
        next_row_index, next_col_index = get_next_move(player_position, command)
        if is_index_valid(next_row_index, len(matrix)) and is_index_valid(next_col_index, len(matrix[0])):
            cell_value = matrix[next_row_index][next_col_index]
            if not cell_value == WALL:
                player_position = [next_row_index, next_col_index]
                path.append(player_position)
                total_coins += cell_value
                if total_coins >= 100:
                    print(f"You won! You've collected {total_coins} coins.")
                    break
            else:
                total_coins = total_coins // 2
                print(f"Game over! You've collected {total_coins} coins.")
                break

        else:
            total_coins = total_coins // 2
            print(f"Game over! You've collected {total_coins} coins.")
            break

print(f"Your path:")
print(*path, sep="\n")