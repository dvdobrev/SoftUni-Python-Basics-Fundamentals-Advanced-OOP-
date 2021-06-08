n = int(input())
n_bombs = int(input())


def read_matrix(n):
    matrix = []

    for row1 in range(n):
        matrix.append([])
        for col1 in range(n):
            matrix[row1].append(0)
    return matrix


matrix = read_matrix(n)


def read_and_deploy_bombs(matrix, n_bombs):
    bombs_positions = []
    for _ in range(n_bombs):
        bp = list(input())
        r, c = int(bp[1]), int(bp[-2])
        bombs_positions.append([r, c])

    for bomb_position in bombs_positions:
        matrix[bomb_position[0]][bomb_position[1]] = '*'

    return bombs_positions


bombs_positions = read_and_deploy_bombs(matrix, n_bombs)

directions = [
    [0, -1],  # left
    [-1, -1],  # left up diagonal
    [-1, 0],  # up
    [-1, 1],  # up right diagonal
    [0, 1],  # right
    [1, 1],  # down right diagonal
    [1, 0],  # down
    [1, -1],  # down left diagonal
]


def is_index_valid(row, col):
    return 0 <= row < n and 0 <= col < n


def check_neighbors(matrix, row, col, directions):
    for direction in directions:
        potential_row, potential_col = row + direction[0], col + direction[1]
        if is_index_valid(potential_row, potential_col):
            if not matrix[potential_row][potential_col] == '*':
                matrix[potential_row][potential_col] += 1
        else:
            continue


for bomb in bombs_positions:
    check_neighbors(matrix, bomb[0], bomb[1], directions)

for row in matrix:
    print(*row)