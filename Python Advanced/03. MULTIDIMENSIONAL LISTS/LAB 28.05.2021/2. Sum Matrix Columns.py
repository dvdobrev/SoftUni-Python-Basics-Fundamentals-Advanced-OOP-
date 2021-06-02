def read_matrix():
    rows_count, colums_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix

def get_colum_sums(matrix):
    rows_count = len(matrix)
    colums_count = len(matrix[0])

    sums = []
    for colum_index in range(colums_count):
        sums.append(0)
        for row_index in range(rows_count):
            sums[-1] += matrix[row_index][colum_index]

    return sums

def print_result(values):
    [print(x) for x in values]

matrix = read_matrix()
result = get_colum_sums(matrix)
print_result(result)
