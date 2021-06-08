def draw_line(count, symbol, first_part_count=0):
    first_part = first_part_count * " "
    second_part = (f"{symbol} " * count).strip()

    print(f"{first_part}{second_part}")


def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, "*", n - i - 1)

    for i in range(n - 2, -1, -1):
        draw_line(i + 1, "*", n - i - 1)


# n = int(input())

draw_rhombus(3)
