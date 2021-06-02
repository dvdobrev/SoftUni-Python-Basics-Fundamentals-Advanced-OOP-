from collections import deque

def read_matrix():
    rows, cols = [int(el) for el in input().split()]
    matrix = []
    for row in range(rows):
        sub_matrix = list(map(int, input().split()))
        matrix.append(sub_matrix)
    return matrix

matrix = read_matrix()
row_size = len(matrix)
col_size = len(matrix[0])
searched_matrix = []
max_sum = -999999999

for row_index in range(row_size - 2):
    current_nums = deque()
    current_sum = 0
    for col_index in range(col_size - 2):
        current_matrix = []
        num1 = matrix[row_index][col_index]
        num2 = matrix[row_index][col_index + 1]
        num3 = matrix[row_index][col_index + 2]
        num4 = matrix[row_index + 1][col_index]
        num5 = matrix[row_index + 1][col_index + 1]
        num6 = matrix[row_index + 1][col_index + 2]
        num7 = matrix[row_index + 2][col_index]
        num8 = matrix[row_index + 2][col_index + 1]
        num9 = matrix[row_index + 2][col_index + 2]
        current_nums.append(num1)
        current_nums.append(num2)
        current_nums.append(num3)
        current_nums.append(num4)
        current_nums.append(num5)
        current_nums.append(num6)
        current_nums.append(num7)
        current_nums.append(num8)
        current_nums.append(num9)
        current_sum = sum(current_nums)
        while current_nums:
            current_list = []
            for el in range(3):
                current_list.append(current_nums.popleft())
            current_matrix.append(current_list)

        if current_sum >= max_sum:
            max_sum = current_sum
            searched_matrix = current_matrix

print(f"Sum = {max_sum}")

# l1 = [str(el) for el in searched_matrix[0]]
# l2 = [str(el) for el in searched_matrix[1]]
# l3 = [str(el) for el in searched_matrix[2]]
# print(" ".join(l1))
# print(" ".join(l2))
# print(" ".join(l3))


for row in range(len(searched_matrix)):
    for col in range(len(searched_matrix)):
        print(searched_matrix[row][col], end=" ")
    print()

