def read_matrix():
    size = int(input())
    matrix = []
    for el in range(size):
        data = [int(el) for el in input().split()]
        submatrix = [x for x in data]
        matrix.append(submatrix)
    return matrix


def primery_diagonal_sum(matrix):
    diagonal_sum = 0
    for row_index in range(len(matrix)):
        for col_index in range(1):
            diagonal_sum += matrix[row_index][row_index]
    return diagonal_sum


def second_diagonal_sum(matrix):
    diagonal_sum = 0
    reversed_matrix = matrix[::-1]
    for row_index in range(len(reversed_matrix)):
        for col_index in range(1):
            diagonal_sum += reversed_matrix[row_index][row_index]
    return diagonal_sum

matrix = read_matrix()
primery_diagonal = primery_diagonal_sum(matrix)
second_diagonal = second_diagonal_sum(matrix)
diff = abs(primery_diagonal - second_diagonal)
print(diff)