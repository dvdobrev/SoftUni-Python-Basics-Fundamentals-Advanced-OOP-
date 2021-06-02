def read_matrix():
    matrix = []

    for row in range(n):
        line = input()
        sub_matrix = [line[el] for el in range(len(line))]
        matrix.append(sub_matrix)

    return matrix


def is_index_valid(value, max_value): # IS INDEX VALID
    return 0 <= value < max_value


def find_kills(row, col, matrix):
    kills_count = 0
    knight_moves = [
        (-1, -2),
        (-2, -1),
        (-2, +1),
        (-1, +2),
        (+1, +2),
        (+2, +1),
        (+2, -1),
        (+1, -2),
    ]
    for el in knight_moves:
        delt_row_index, delta_col_index = el
        row_move = delt_row_index + row
        col_move = delta_col_index + col
        if is_index_valid(row_move, n) and is_index_valid(col_move, n):
            if matrix[row_move][col_move] == "K":
                kills_count += 1

    return kills_count


n = int(input())
matrix = read_matrix()


knight_row_pos = 0
knight_col_pos = 0
removed_knights = 0

while True:
    max_kills = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                kills = find_kills(row, col, matrix)
                if kills > max_kills:
                    max_kills = kills
                    knight_row_pos = row
                    knight_col_pos = col

    if max_kills == 0:
        break

    matrix[knight_row_pos][knight_col_pos] = 0
    removed_knights += 1

print(removed_knights)