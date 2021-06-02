n = int(input())
matrix = [(list(map(int, input().split()))) for row in range(n)]

data = input()

while not data == "END":
    command, row, col, value = data.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if col < 0 or row < 0:
        print(f"Invalid coordinates")
        data = input()
        continue
    try:
        if command == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value

    except IndexError:
        print(f"Invalid coordinates")

    data = input()

print(*[' '.join(map(str, row)) for row in matrix], sep="\n")