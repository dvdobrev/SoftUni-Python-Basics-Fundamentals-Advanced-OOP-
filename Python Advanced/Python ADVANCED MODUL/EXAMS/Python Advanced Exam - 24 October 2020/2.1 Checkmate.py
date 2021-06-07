def read_board():
    board = []

    for i in range(8):
        m = input().split()
        board.append(m)
    return board

def find_king_position(board):
    for row_index in range(len(board)):
        for column_index in range(len(board[0])):
            if board[row_index][column_index] == "K":
                return (row_index, column_index)

# def get_capturing_queens(board, king):
#     rows_count = len(board)
#     columns_count = len(board[0])
#     (king_row_index, king_column_index) = king
#     queens = []
#     # right
#     for column_index in range(king_column_index + 1, columns_count):
#         if board[king_row_index][column_index] == "Q":
#             queens.append((king_row_index, column_index))
#             break
#     #left
#     for column_index in range(king_column_index - 1, -1, -1):
#         if board[king_row_index][column_index] == "Q":
#             queens.append((king_row_index, column_index))
#             break
#
#     return queens

def in_range(value, max_value):
    return 0 <= value < max_value

def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    columns_count = len(board[0])
    (delta_row, delta_column) = deltas
    (row_index, column_index) = king


    while True:
        if not in_range(row_index, rows_count) or not in_range(column_index, columns_count):
            return None

        if board[row_index][column_index] == "Q":
            return (row_index, column_index)

        row_index += delta_row
        column_index += delta_column


def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1),
    ]

    queens = [search_with_deltas(board, king, delta) for delta in deltas]
    print(queens)
    return [queen for queen in queens if queen]

def print_result(queens):
    if queens:
        for queen in queens:
            print(list(queen))
    else:
        print("The king is safe!")

board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)