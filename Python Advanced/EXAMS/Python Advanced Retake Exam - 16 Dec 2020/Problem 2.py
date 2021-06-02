PLAYER = "P"


def read_matrix(n):
    matrix = [list(input()) for _ in range(n)]

    return matrix


def find_the_player(matrix):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if PLAYER == char:
                return y, x


def move(dy, dx, t, matrix):
    global text, player_position

    y, x = player_position
    new_y = y + dy
    new_x = x + dx
    if new_y < 0 or new_y >= row_col_num or new_x < 0 or new_x >= row_col_num:
        if text:
            text = text[:-1]
        return

    else:
        matrix[y][x] = "-"
        symbol = matrix[new_y][new_x]
        if symbol == "-":
            matrix[new_y][new_x] = PLAYER
        else:
            text += symbol
            matrix[new_y][new_x] = PLAYER

    player_position = (new_y, new_x)
    return text, matrix, player_position


text = input()
row_col_num = int(input())
matrix = read_matrix(row_col_num)
player_position = find_the_player(matrix)

commands_num = int(input())

commands = {
    "up": lambda: move(-1, 0, text, matrix),
    "down": lambda: move(1, 0, text, matrix),
    "left": lambda: move(0, -1, text, matrix),
    "right": lambda: move(0, 1, text, matrix),

}

for i in range(commands_num):
    command = input()
    command_fn = commands[command]
    command_fn()

print(text)
for el in matrix:
    el = [''.join("".join(a) for a in el)]
    print(*el)
