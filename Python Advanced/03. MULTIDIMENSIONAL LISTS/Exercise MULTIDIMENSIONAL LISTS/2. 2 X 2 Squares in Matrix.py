def read_matrix():
    n = input()
    rows_counts, col_counts = list(map(int, n.split()))
    matrix = []

    for rows in range(rows_counts):
        row = list(map(str, input().split()))
        matrix.append(row)
    return matrix

def equal_char(matrix, size):
    equal_char_counter = 0
    for row in range(size):
        for col in range(len(matrix[0]) - 1):
            first_char = matrix[row][col]
            second_char = matrix[row][col + 1]
            third_char = matrix[row + 1][col]
            forth_char = matrix[row + 1][col + 1]
            char_list = list(first_char * 4)
            check_char_list = [first_char, second_char, third_char, forth_char]
            if char_list == check_char_list:
                equal_char_counter += 1
    return equal_char_counter

matrix = read_matrix()
size = len(matrix) - 1
char_couples = equal_char(matrix, size)
print(char_couples)