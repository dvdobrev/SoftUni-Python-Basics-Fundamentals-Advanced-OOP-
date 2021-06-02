def read_matrix():
    rows_count, colums_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)
    return matrix

def get_sum_of_submatrix(matrix, row_index, colum_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(colum_index, colum_index + size):
            the_sum += matrix[r][c]
    return the_sum

def get_best_submatrix_sum(matrix, submatrix_size):
    best_row_index = 0
    best_colum_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for colum_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, colum_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_colum_index = colum_index
    return (best_row_index, best_colum_index)

def print_result(coordinates, size):
    (row_index, colum_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(colum_index, colum_index + size):
            row.append(matrix[r][c])
        print(" ".join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, colum_index, size))

matrix = read_matrix()
submatrix_size = 2

print_result(get_best_submatrix_sum(matrix, submatrix_size), submatrix_size)