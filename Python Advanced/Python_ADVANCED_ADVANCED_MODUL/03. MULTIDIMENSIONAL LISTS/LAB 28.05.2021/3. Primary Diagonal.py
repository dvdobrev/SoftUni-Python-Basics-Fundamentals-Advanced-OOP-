def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)
    return matrix

def get_sum_of_primary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

def get_sum_below_primery_diagonal(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            if c <= r:
                the_sum += matrix[r][c]


def get_sum_above_primery_diagonal(matrix):
    the_sum = 0
    size = len(matrix)
    for r in range(size):
        for c in range(r, size):
            the_sum += matrix[r][c]
    return the_sum


def get_sum_of_secondary_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]
    return diagonal_sum

print(get_sum_of_primary_diagonal(read_matrix()))