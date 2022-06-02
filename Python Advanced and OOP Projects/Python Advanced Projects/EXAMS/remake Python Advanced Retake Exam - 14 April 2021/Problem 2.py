pl1, pl2 = input().split(', ')
n = 7


def read_matrix(n):
    matrix = []

    for row in range(n):
        current_row = list(input().split())
        for index, el in enumerate(current_row):
            if not el.isalpha():
                current_row[index] = int(el)

        matrix.append(current_row)

    return matrix


def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value


def get_next_move(row, col, dir):
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return row + row_delta, col + column_delta


def next_num(row, col, dir):
    while True:
        next_row_index, next_col_index = get_next_move(row, col, dir)
        target = str(matrix[next_row_index][next_col_index])

        if target.isdigit():
            number = int(matrix[next_row_index][next_col_index])
            return number

        else:
            row = next_row_index
            col = next_col_index


def hitted_target(row, col):
    if hited_point == "D":
        up_number = next_num(row, col, "up")
        down_number = next_num(row, col, "down")
        right_number = next_num(row, col, "right")
        left_number = next_num(row, col, "left")

        return (up_number + down_number + right_number + left_number) * 2

    elif hited_point == "T":
        up_number = next_num(row, col, "up")
        down_number = next_num(row, col, "down")
        right_number = next_num(row, col, "right")
        left_number = next_num(row, col, "left")

        return (up_number + down_number + right_number + left_number) * 3

    elif hited_point == "B":
        return 501

    else:
        return matrix[row][col]


matrix = read_matrix(n)

pl1_score = 501
pl1_throws = 0

pl2_score = 501
pl2_throws = 0
turn_count = 1
current_player = None
have_winner = False

while not have_winner:
    row, col = eval(input())

    if turn_count == 1:
        pl1_throws += 1
        current_player = pl1
        turn_count = 2

        if is_index_valid(row, 8) and is_index_valid(col, 8):
            hited_point = matrix[row][col]
            pl1_score -= hitted_target(row, col)
            if pl1_score <= 0:
                have_winner = True
                print(f"{pl1} won the game with {pl1_throws} throws!")

    else:
        pl2_throws += 1
        current_player = pl2
        turn_count = 1

        if is_index_valid(row, 8) and is_index_valid(col, 8):
            hited_point = matrix[row][col]
            pl2_score -= hitted_target(row, col)
            if pl2_score <= 0:
                have_winner = True
                print(f"{pl2} won the game with {pl2_throws} throws!")
