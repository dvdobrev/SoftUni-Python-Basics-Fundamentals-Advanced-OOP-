PLAYER = "P"
BUNNY = "B"

'''
y = row , x = col. Пиша ги така, гледайки матрицата като координатна система, където row са на оста ,x са на оста 
'''

def read_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = []

    for row in range(rows):
        line = input()
        sub_matrix = [line[el] for el in range(len(line))]
        matrix.append(sub_matrix)

    return matrix


def find_player(m):
    player_pos = ()
    for y, rows in enumerate(m):
        for x, cols in enumerate(rows):
            if cols == PLAYER:
                player_pos = (y, x)

    return player_pos


def find_buny(m):
    bunny_pos = []
    for y, rows in enumerate(m):
        current_bunny_pos = ()
        for x, cols in enumerate(rows):
            if cols == BUNNY:
                current_bunny_pos = (y, x)
                bunny_pos.append(current_bunny_pos)

    return bunny_pos


def valid_y_index(index):
    return 0 <= index < len(matrix)


def valid_x_index(index):
    return 0 <= index < len(matrix[0])


def bunnys_mutate_fn(m, b_pos):
    for el in b_pos:
        y = el[0]
        x = el[1]
        if valid_y_index(y + 1):
            m[y + 1][x] = BUNNY
        if valid_y_index(y - 1):
            m[y - 1][x] = BUNNY
        if valid_x_index(x + 1):
            m[y][x + 1] = BUNNY
        if valid_x_index(x - 1):
            m[y][x - 1] = BUNNY
    return m, b_pos


def move(dy, dx):
    global player_position, moves_count, matrix, bunnys_positions, is_dead, is_out, new_x, new_y
    y, x = player_position
    new_x = x + dx
    new_y = y + dy
    symbol = matrix[new_y][new_x]
    if new_x < 0 or new_y < 0 or new_y >= len(matrix) or new_x >= len(matrix[0]): # is out
        is_out = True
        matrix[y][x] = "."
        bunnys_mutate = bunnys_mutate_fn(matrix, bunnys_positions)
        return y, x

    else:
        if symbol == ".": # is still in
            matrix[y][x] = "."
            matrix[new_y][new_x] = PLAYER
            bunnys_mutate = bunnys_mutate_fn(matrix, bunnys_positions)
            player_position = find_player(matrix)
            if not player_position:
                is_dead = True

            bunnys_positions = find_buny(matrix)

        else:
            bunnys_mutate = bunnys_mutate_fn(matrix, bunnys_positions) # is dead
            is_dead = True
            return new_y, new_x

matrix = read_matrix()
player_position = find_player(matrix)
bunnys_positions = find_buny(matrix)
new_x = 0
new_y = 0
move_commands = [el for el in input()]

moves = {
    "U": lambda: move(-1, 0),
    "D": lambda: move(+1, 0),
    "L": lambda: move(0, -1),
    "R": lambda: move(0, +1)
}

is_dead = False
is_out = False
for el in move_commands:
    move_fn = moves[el]
    move_fn()
    if is_out:
        y, x = move_fn()
        print(*[''.join(el) for el in matrix], sep="\n")
        print(f"won: {y} {x}")
        break
    if is_dead:
        #y, x = move_fn()
        print(*[''.join(el) for el in matrix], sep="\n")
        #print(f"dead: {y} {x}")
        print(f"dead: {new_y} {new_x}")
        break