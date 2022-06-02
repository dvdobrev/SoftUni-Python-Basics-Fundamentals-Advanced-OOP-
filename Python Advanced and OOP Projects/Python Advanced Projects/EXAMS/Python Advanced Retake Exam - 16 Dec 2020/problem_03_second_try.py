def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    for row in range(2, n):
        sub_matrix = []
        for col in range(row + 1):
            if col == 0:
                current_cell = matrix[row - 1][col]
                sub_matrix.append(current_cell)
            elif 0 < col < row:
                current_cell = matrix[row - 1][col - 1] + matrix[row - 1][col]
                sub_matrix.append(current_cell)
            else:
                current_cell = matrix[row - 1][col - 1]
                sub_matrix.append(current_cell)

        matrix.append(sub_matrix)
    return matrix


get_magic_triangle(5)
