def read_matrix():
    num = int(input())
    matrix = [[int(el) for el in input().split(", ")] for _ in range(num)]
    return matrix

def get_even_matrix(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]

def print_result(matrix):
    print(matrix)

matrix = read_matrix()
even_matrix = get_even_matrix(matrix)
print_result(even_matrix)
