import re


def read_matrix():
    n = int(input())
    matrix = []

    for row in range(n):
        line = "."*n
        sub_matrix = [line[el] for el in range(n)]
        matrix.append(sub_matrix)

    return matrix


def get_cordinates(text):

    pattern = r"[0-9]+"
    result = re.findall(pattern, text)
    row, col = [int(el) for el in result]
    return row, col



def is_index_valid(value, max_value):
    return 0 <= value < max_value



def find_bombs(row, col, matrix):
    mine_counter = 0
    for (r, c) in directions:
        next_row = row + r
        next_col = col + c

        if is_index_valid(next_row, len(matrix)) and is_index_valid(next_col, len(matrix)):
            if matrix[next_row][next_col] == "*":
                mine_counter += 1
    return mine_counter



def find_cell(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == ".":
                bombs_count = find_bombs(row, col, matrix)
                matrix[row][col] = bombs_count

matrix = read_matrix()
bombs_number = int(input())
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

for i in range(bombs_number):
    text = input()
    row, col = get_cordinates(text)
    matrix[row][col] = "*"

bombs_for_cell = find_cell(matrix)

for el in matrix:
    print(*el)