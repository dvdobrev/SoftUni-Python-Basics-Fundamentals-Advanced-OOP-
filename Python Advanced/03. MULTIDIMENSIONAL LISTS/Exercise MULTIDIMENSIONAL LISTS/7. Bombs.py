def read_matrix():
    matrix = []

    for row in range(n):
        line = input().split()
        sub_matrix = list(map(int, line))
        matrix.append(sub_matrix)

    return matrix


def is_index_valid(value, max_value, new_cordinates):  # IS INDEX VALID
    if new_cordinates not in bomb_cordinates and 0 <= value < max_value:
        return True


def bomb_explode(bomb, matrix, bomb_value):
    row, col = bomb
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
    for el in directions:
        delta_row, delta_col = el
        next_row_index = delta_row + row
        next_col_index = delta_col + col
        new_cordinates = (next_row_index, next_col_index)

        if is_index_valid(next_row_index, n, new_cordinates) and is_index_valid(next_col_index, n, new_cordinates):
            current_cell_value = matrix[next_row_index][next_col_index]

            if not current_cell_value <= 0:
                matrix[next_row_index][next_col_index] -= bomb_value  # change the value on cell


def find_active_cells(matrix):
    cells_count = 0
    cell_sums = 0
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if matrix[r][c] > 0:
                cell_sums += matrix[r][c]
                cells_count += 1

    return (cells_count, cell_sums)


n = int(input())
matrix = read_matrix()

bomb_cordinates = [tuple(int(l) for l in el if l.isnumeric()) for el in input().split()]

for bomb in bomb_cordinates:
    row, col = bomb
    bomb_value = matrix[row][col]
    new_matrix_values = bomb_explode(bomb, matrix, bomb_value)
    matrix[row][col] = 0  # after the bomb exploed

active_cells, cell_sum = find_active_cells(matrix)

print(f"Alive cells: {active_cells}")
print(f"Sum: {cell_sum}")

for el in matrix:
    print(*el)