SNAKE = "S"
LAIR = "B"
FOOD = "*"
FREE_CELL = "-"

def read_matrix():
    matrix = []

    for row in range(n):
        line = input()
        sub_matrix = [line[el] for el in range(len(line))]
        matrix.append(sub_matrix)

    return matrix


def find_the_snake(matrix):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if SNAKE == char:
                return (y, x)


def find_the_lair(matrix):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if LAIR == char:
                return (y, x)


def find_next_move(row, col, dir):  # DIRECTIONS FUNKTION
    dir_deltas = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }
    (row_delta, column_delta) = dir_deltas[dir]

    return (row + row_delta, col + column_delta)


def is_index_valid(value, max_value): # IS INDEX VALID
    return 0 <= value < max_value


n = int(input())
matrix = read_matrix()
snake_row_index, snake_col_index = find_the_snake(matrix)
food_count = 0


while True:
    command = input()
    new_row_index, new_col_index = find_next_move(snake_row_index, snake_col_index, command)
    if is_index_valid(new_row_index, len(matrix)) and is_index_valid(new_col_index, len(matrix[0])):
        if matrix[new_row_index][new_col_index] == FREE_CELL:
            matrix[new_row_index][new_col_index] = SNAKE
            matrix[snake_row_index][snake_col_index] = "."
            snake_row_index, snake_col_index = new_row_index, new_col_index

        elif matrix[new_row_index][new_col_index] == LAIR:
            matrix[new_row_index][new_col_index] = "."
            matrix[snake_row_index][snake_col_index] = "."
            snake_row_index, snake_col_index = find_the_lair(matrix)
            matrix[snake_row_index][snake_col_index] = SNAKE

        else:
            matrix[new_row_index][new_col_index] = SNAKE
            matrix[snake_row_index][snake_col_index] = "."
            snake_row_index, snake_col_index = new_row_index, new_col_index
            food_count += 1
            if food_count >= 10:
                print(f"You won! You fed the snake.")
                print(f"Food eaten: {food_count}")
                break

    else:  # is out
        matrix[snake_row_index][snake_col_index] = "."
        print(f"Game over!")
        print(f"Food eaten: {food_count}")
        break

[print("".join(el)) for el in matrix]