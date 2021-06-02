from collections import deque

def read_matrix():
    rows_count, col_count = map(int, input().split())
    matrix = []
    for row in range(rows_count):
        current_list = []
        for col in range(col_count):
            current_list.append(col)
        matrix.append(current_list)

    return matrix

matrix = read_matrix()
snake = deque(input())
counter = 1

for row in range(len(matrix)):
    col_len = len(matrix[0])
    if not counter % 2 == 0:
        for col in range(col_len):
            current_char = snake.popleft()
            snake.append(current_char)
            matrix[row][col] = current_char
    else:
        for col in range(col_len - 1, -1, -1):
            current_char = snake.popleft()
            snake.append(current_char)
            matrix[row][col] = current_char
    counter += 1
    print("".join(matrix[row]))