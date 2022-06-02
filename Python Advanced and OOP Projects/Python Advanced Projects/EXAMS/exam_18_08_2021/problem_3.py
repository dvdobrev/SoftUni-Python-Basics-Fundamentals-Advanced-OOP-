def fill_the_box(height, length, width, *args):
    box_size = height * length * width

    total_cubs = len(args) - 1
    total_cubs_size = 0

    for c in range(total_cubs):
        if args[c] == 'Finish':
            continue
        total_cubs_size += args[c]


    for i in range(total_cubs):
        arg = args[i]
        if arg == "Finish":
            return f"There is free space in the box. You could put {box_size} more cubes."


        if box_size <= arg:
            total_cubs_size -= box_size
            return f"No more free space! You have {total_cubs_size} more cubes."

        else:
            box_size -= arg
            total_cubs_size -= arg

    return f"There is free space in the box. You could put {box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
