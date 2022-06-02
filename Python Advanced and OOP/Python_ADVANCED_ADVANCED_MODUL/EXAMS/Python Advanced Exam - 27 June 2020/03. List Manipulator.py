def list_manipulator(*args):
    text = args
    list_numbers = args[0]
    first_command = args[1]
    second_command = args[2]
    try:
        number = args[3]
        if first_command == "remove":
            if second_command == "beginning":
                list_numbers = list_numbers[number:]
            elif second_command == "end":
                list_numbers = list_numbers[:-number]


        elif first_command == "add":
            numbers = list(text[3:])
            if second_command == "beginning":
                numbers.extend(list_numbers)
                list_numbers = numbers

            elif second_command == "end":
                list_numbers.extend(numbers)

    except IndexError:
        if first_command == "remove":
            if second_command == "beginning":
                list_numbers.pop(0)
            elif second_command == "end":
                list_numbers.pop()

    return list_numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
