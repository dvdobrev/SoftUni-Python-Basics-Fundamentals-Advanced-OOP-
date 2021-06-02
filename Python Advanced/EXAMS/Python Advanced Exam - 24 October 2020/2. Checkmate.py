def read_matrix():
    matrix = []

    for i in range(8):
        m = input().split()
        matrix.append(m)

    return matrix


def moves_row_down(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r + 1][c] == ".":
                    r += 1
                    continue
                elif matrix[r + 1][c] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_row_up(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r - 1][c] == ".":
                    r -= 1
                    continue
                elif matrix[r - 1][c] == "K" and not r <= 0:
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_col_right(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r][c + 1] == ".":
                    c += 1
                    continue
                elif matrix[r][c + 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_col_left(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r][c - 1] == ".":
                    c -= 1
                    continue
                elif matrix[r][c - 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_diagonal_right_up(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r - 1][c + 1] == ".":
                    r -= 1
                    c += 1
                    continue
                elif matrix[r - 1][c + 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_diagonal_right_down(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r + 1][c + 1] == ".":
                    r += 1
                    c += 1
                    continue
                elif matrix[r + 1][c + 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_diagonal_left_down(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r + 1][c - 1] == ".":
                    r += 1
                    c -= 1
                    continue
                elif matrix[r + 1][c - 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


def moves_diagonal_left_up(matrix, r, c, is_v):
    if not is_v:
        queen_position = [r, c]
        while not r < 0 and not c < 0:
            try:
                if matrix[r - 1][c - 1] == ".":
                    r -= 1
                    c -= 1
                    continue
                elif matrix[r - 1][c - 1] == "K":
                    print(queen_position)
                    is_v = True
                    break
                else:
                    break
            except IndexError:
                break

    return is_v


matrix = read_matrix()
queens_counter = 0
for row in range(len(matrix)):
    col_lenght = len(matrix[row])
    for col in range(col_lenght):
        is_valid = False
        if matrix[row][col] == "Q":
            is_valid = moves_row_up(matrix, row, col, is_valid)
            is_valid = moves_row_down(matrix, row, col, is_valid)
            is_valid = moves_col_right(matrix, row, col, is_valid)
            is_valid = moves_col_left(matrix, row, col, is_valid)
            is_valid = moves_diagonal_right_up(matrix, row, col, is_valid)
            is_valid = moves_diagonal_right_down(matrix, row, col, is_valid)
            is_valid = moves_diagonal_left_down(matrix, row, col, is_valid)
            is_valid = moves_diagonal_left_up(matrix, row, col, is_valid)
        if is_valid:
            queens_counter += 1

if queens_counter == 0:
    print(f"The king is safe!")