from collections import deque

BUNNY = "B"
PLAYER = "P"
EMPTY = "."

def read_input():
    rows_count, columns_count = [int(x) for x in input().split(" ")]
    lair =[]
    for _ in range(rows_count):
        lair.append(list(input()))
    directions = input()

    return (lair, directions)

def in_range(value, max_value):
    return 0 <= value < max_value


def get_bunnies(lair):
    bunnis = []
    for row_index in range(len(lair)):
        for coulumn_index in range(len(lair[0])):
            if lair[row_index][coulumn_index] == BUNNY:
                bunnis.append([row_index, coulumn_index])
    return bunnis


def get_player(lair):
    for row_index in range(len(lair)):
        if PLAYER in lair[row_index]:
            column_index = lair[row_index].index(PLAYER)
            return (row_index, column_index)



def get_next_move(position, dir):
    dir_deltas = {
        "U": (-1, 0),
        "D": (+1, 0),
        "L": (0, -1),
        "R": (0, +1),
    }
    (row_indx, column_index) = position
    (row_delta, column_delta) = dir_deltas[dir]

    return row_indx + row_delta, column_index + column_delta


def is_free_cell(lair, position):
    rows_count = len(lair)
    columns_count = len(lair[0])
    (row_index, column_index) = position

    return in_range(row_index, rows_count) \
           and in_range(column_index, columns_count) \
           and not lair[row_index][column_index] == BUNNY


def spread_bunnies(lair, bunnies):
    for _ in range(len(bunnies)):
        bunny = bunnies.popleft()
        next_bunnies = [get_next_move(bunny, dir) for dir in "UDRL"]
        next_bunnies = [next_bunny for next_bunny in next_bunnies if is_free_cell(lair, next_bunny)]

        for (row_index, col_index) in next_bunnies:
            lair[row_index][col_index] = BUNNY
            bunnies.append((row_index, col_index))



def is_win(lair, player):
    (row_index, column_index) = player
    return not in_range(row_index, len(lair)) \
           or not in_range(column_index, len(lair[0]))


def is_loss(lair, player):
    (row_index, column_index) = player
    return lair[row_index][column_index] == BUNNY



def print_result(lair, player, is_win):
    row_index, column_index = player
    [print("".join(row)) for row in lair]
    if is_win:
        print(f"won: {row_index} {column_index}")

    else:
        print(f"dead: {row_index} {column_index}")



# ot tuk  e bez promqna
def play_game(lair, bunnies, player, directions):
    bunnies = deque(bunnies)

    is_dead = False

    for dir in directions:
        row_index, column_index = player

        if not is_dead:

            next_row_index, next_column_index = get_next_move((row_index, column_index), dir)

            if is_win(lair, (next_row_index, next_column_index)):
                lair[row_index][column_index] = EMPTY
                spread_bunnies(lair, bunnies)
                print_result(lair, (row_index, column_index), is_win=True)
                break

            else:
                if lair[next_row_index][next_column_index] == EMPTY:   # move to the next cell. And afeter that have to check if the player is not dead after the bunnies splieting them selfs
                    lair[next_row_index][next_column_index] = PLAYER
                    lair[row_index][column_index] = EMPTY
                    spread_bunnies(lair, bunnies)
                    player = get_player(lair)
                    if not player: # is dead because a bunny meet the plaer
                        is_dead = True
                        [print("".join(row)) for row in lair]
                        print(f"dead: {next_row_index} {next_column_index}")
                        return (next_row_index, next_column_index)

                else:  # is dead because the player meet a Bunny
                    spread_bunnies(lair, bunnies)
                    is_dead = True
                    [print("".join(row)) for row in lair]
                    print(f"dead: {next_row_index} {next_column_index}")

        else:
            break


    # for dir in directions:
    #     spread_bunnies(lair, bunnies)
    #     next_row_index, next_column_index = get_next_move((row_index, column_index), dir)
    #
    #     if is_win(lair, (next_row_index, next_column_index)):
    #         lair[row_index][column_index] = EMPTY
    #         print_result(lair, (row_index, column_index), is_win=True)
    #         break
    #
    #     elif is_loss(lair, (next_row_index, next_column_index)):
    #         print_result(lair, (next_row_index, next_column_index), is_win=False)
    #         break
    #
    #     lair[row_index][column_index] = EMPTY
    #     lair[next_row_index][next_column_index] = PLAYER
    #     row_index, column_index = next_row_index, next_column_index


lair, directions = read_input()
bunnies = get_bunnies(lair)
player = get_player(lair)

play_game(lair, bunnies, player, directions)