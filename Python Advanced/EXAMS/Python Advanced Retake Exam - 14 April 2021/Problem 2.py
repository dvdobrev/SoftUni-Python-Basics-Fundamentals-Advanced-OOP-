import re

p1, p2 = input().split(", ")

def read_input():
    matrix = []
    for _ in range(7):
        matrix.append(list(input().split()))

    return matrix

def get_cordinates(text):

    pattern = r"[0-9]+"
    result = re.findall(pattern, text)
    row, col = [int(el) for el in result]
    return row, col


def target_result(matrix, row, col):
    if not row > 6 and not col > 6:

        hited_target = matrix[row][col]

        if hited_target.isnumeric():
            hited_target = int(hited_target)
            return hited_target
        elif hited_target == "D":
            total_points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
            return total_points
        elif hited_target == "T":
            total_points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
            return total_points
        else:
            total_points = 10000
            return total_points

    else:
        return 0

matrix = read_input()
text = input()
players_turn = 1
p1_points = 501
p1_turns = 0
p2_points = 501
p2_turns = 0

while True:
    row, col = get_cordinates(text)
    if players_turn == 1:
        p1_turns += 1
        players_turn = 2
        points = target_result(matrix, row, col)
        p1_points -= points
        if p1_points <= 0:
            print(f"{p1} won the game with {p1_turns} throws!")
            break

        elif p1_points > 1000:
            print(f"{p1} won the game with {p1_turns} throws!")
            break

    else:
        p2_turns += 1
        players_turn = 1
        points = target_result(matrix, row, col)
        p2_points -= points
        if p2_points <= 0:
            print(f"{p2} won the game with {p2_turns} throws!")
            break

        elif p2_points > 1000:
            print(f"{p2} won the game with {p2_turns} throws!")
            break

    text = input()