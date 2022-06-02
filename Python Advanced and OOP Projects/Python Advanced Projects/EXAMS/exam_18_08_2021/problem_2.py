ALICE = "A"
RABBIT = "R"
FREE_SPACE = "."


def read_matrix(n):
    matrix = []

    alice_row_index = None
    alice_col_index = None

    rabbit_row_index = None
    rabbit_col_index = None

    for row in range(n):
        current_row = list(input().split())
        if ALICE in current_row:
            alice_row_index = row
            alice_col_index = current_row.index(ALICE)

        if RABBIT in current_row:
            rabbit_row_index = row
            rabbit_col_index = current_row.index(RABBIT)

        for index, el in enumerate(current_row):
            if el.isnumeric():
                current_row[index] = int(el)

        matrix.append(current_row)

    return (matrix, alice_row_index, alice_col_index, rabbit_row_index, rabbit_col_index)


def is_index_valid(value, max_value):
    return 0 <= value < max_value


def is_rabbit(matrix, row, col):
    if matrix[row][col] == RABBIT:
        return True
    else:
        return False


def get_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return row + row_delta, col + column_delta


n = int(input())
matrix, alice_row_index, alice_col_index, rabbit_row_index, rabbit_col_index = read_matrix(n)
collected_bags = 0
she_did_it = False

while not she_did_it:
    command = input()
    next_row_index, next_col_index = get_next_move(alice_row_index, alice_col_index, command)

    if not is_index_valid(next_row_index, n):
        print("Alice didn't make it to the tea party.")
        matrix[alice_row_index][alice_col_index] = "*"
        break

    if not is_index_valid(next_col_index, n):
        print("Alice didn't make it to the tea party.")
        matrix[alice_row_index][alice_col_index] = "*"
        break

    if (rabbit_row_index, rabbit_col_index) == (next_row_index, next_col_index):

        print("Alice didn't make it to the tea party.")
        matrix[alice_row_index][alice_col_index] = "*"
        matrix[next_row_index][next_col_index] = "*"
        break

    else:
        if matrix[next_row_index][next_col_index] == FREE_SPACE or matrix[next_row_index][next_col_index] == "*":
            matrix[alice_row_index][alice_col_index] = "*"
            alice_row_index, alice_col_index = next_row_index, next_col_index
            matrix[alice_row_index][alice_col_index] = "*"

        else:
            matrix[alice_row_index][alice_col_index] = "*"
            num = matrix[next_row_index][next_col_index]
            collected_bags += num
            alice_row_index, alice_col_index = next_row_index, next_col_index
            matrix[alice_row_index][alice_col_index] = "*"

            if collected_bags >= 10:
                she_did_it = True
                print("She did it! She went to the party.")

    # print(*matrix, sep="\n")
    # print()

# print(*matrix, sep="\n")

for el in matrix:
    a = [str(i) for i in el]
    el = "".join(' '.join([a for a in a]))

    print(el)
