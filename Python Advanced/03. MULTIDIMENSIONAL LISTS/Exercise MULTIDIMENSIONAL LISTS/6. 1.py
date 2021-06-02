n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

def is_valid(matrix, r, c):
    if 0 <= r < n and c <= 0 < n:
        return True
    return False

def check_position(matrix, row, col):
    rows = [-2, -2, 2, 2, -1, -1, 1, 1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    killer_position = []
    kills = 0
    for index in range(len(rows)):
        potentional_row = row + row[index]
        potentional_col = col + col[index]
        if is_valid:
            killer_position = [row, col]
            kills += 1


for row_index in range(len(matrix[0])):
    for col_index in range(len(matrix[0])):

