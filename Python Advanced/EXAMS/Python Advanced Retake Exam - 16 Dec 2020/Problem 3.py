def get_magic_triangle(n):
    matrix = []
    for row in range(n):
        sub_matrix = []
        for col in range(row + 1):
            if row > 1:
                first_number = 0
                second_num = 0
                if col - 1 < 0:
                    first_number = (matrix[row - 1][0])

                elif col + 1 > len(matrix[row - 1]):
                    second_num = matrix[row - 1][-1]

                else:
                    first_number = matrix[row - 1][col - 1]
                    second_num = matrix[row - 1][col]

                total = first_number + second_num

                sub_matrix.append(total)

            else:
                sub_matrix.append(1)


        matrix.append(sub_matrix)

    return matrix

#get_magic_triangle(5)