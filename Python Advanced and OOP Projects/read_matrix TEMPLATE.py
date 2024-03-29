def read_matrix(n):  # Finde PLAYER AND Read, Matrix. !!! Return all - Matrix, player_row, player_col !!!!!
    matrix = []
    player_row_index = None
    player_col_index = None

    for row in range(n):
        current_row = list(input().split())
        if "P" in current_row:
            player_row_index = row
            player_col_index = current_row.index("P")

        matrix.append(current_row)

    return (matrix, player_row_index, player_col_index)


matrix, player_row_index, player_col_index = read_matrix(n)
print(*matrix, sep="\n")

-----------------------------------------------------------


def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = []

    for row in range(rows):
        line = input()  # може да е и със .SPLIT
        sub_matrix = [line[el] for el in range(len(line))]
        # sub_matrix = list(map(int, line))  # ако ми трябват да са интиджер
        matrix.append(sub_matrix)

    return matrix


matrix = read_matrix()
print(*matrix, sep="\n")

-----------------------------------------------------------------


def read_input():
    rows_count, columns_count = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(rows_count):
        matrix.append(list(input().split()))  # може да е и без .SPLIT

    return matrix


matrix = read_input()
print(*matrix, sep="\n")

---------------------------------------------------------------------------


def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value


------------------------------------------------------------------------


def find_the_player(matrix):  # Find the thing we search
    for row_index, row in enumerate(matrix):
        for col_index, char in enumerate(row):
            if PLAYER == char:
                return row_index, col_index


--------------------------------------------------------------------------------


def get_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_index, column_index) = position
    (row_delta, column_delta) = dir_deltas[dir]

    return row_index + row_delta, column_index + column_delta


# DOLNATA \ FOR ALL DIREKTIONS + DIAGONALS
directions = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
]

---------------------------------------------------------------------------
FORMATING
b = ', '.join([el for el in test])
a = ', '.join([f"{k}: {v}" for k, v in self.ingredients.items()])


a = ["15", "29"]
b = "".join(', '.join([el for el in a]))

--> 15, 29

--------------------------------------------------------------------

from collections import defaultdict

a = defaultdict(lambda: 0)  # If there is not a key and value the default dict makes a such one!!!
a["some_key"] += "some_value"
