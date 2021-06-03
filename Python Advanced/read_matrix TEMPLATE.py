def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = []

    for row in range(rows):
        line = input()  # може да е и със .SPLIT
        sub_matrix = [line[el] for el in range(len(line))]
        #sub_matrix = list(map(int, line))  # ако ми трябват да са интиджер
        matrix.append(sub_matrix)

    return matrix

matrix = read_matrix()
print(*matrix, sep="\n")


def read_input():
    rows_count, columns_count = [int(x) for x in input().split(" ")]
    matrix =[]
    for _ in range(rows_count):
        matrix.append(list(input().split()))  # може да е и без .SPLIT

    return matrix

matrix = read_input()

print(*matrix, sep="\n")



def is_index_valid(value, max_value):  # IS INDEX VALID
    return 0 <= value < max_value



def find_the_player(matrix):  # Find the thing we search
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if PLAYER == char:
                return y, x


def get_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "U": (-1, 0),
        "D": (+1, 0),
        "L": (0, -1),
        "R": (0, +1),
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
