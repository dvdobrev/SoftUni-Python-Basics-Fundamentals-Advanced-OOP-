def read_matrix():
    num = int(input())
    matrix = [[int(el) for el in input().split(", ")] for _ in range(num)]
    return matrix

matrix = read_matrix()
a = [x for row in matrix for x in row]
print(a)

# def read_matrix():
#     rows_counts = int(input())
#     return [input().split(", ") for _ in range(rows_counts)]
#
# def flatten(matrix):
#     return [x for row in matrix for x in row]
#
# def print_result(values):
#     print([int(x) for x in values])
#
# matrix = read_matrix()
# result = flatten(matrix)
# print_result(result)