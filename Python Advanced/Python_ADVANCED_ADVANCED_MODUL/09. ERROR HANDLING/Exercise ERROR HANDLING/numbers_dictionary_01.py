#command = input()
dictionary = {}

while True:
    number_as_string = input()
    if number_as_string == "Search":
        break

    try:
        number = int(input())
        dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")

command = input()

while not command == "Remove":
    searched_number = command

    try:
        print(dictionary[searched_number])

    except KeyError:
        print("Number does not exist in dictionary")

    command = input()

command = input()

while not command == "End":
    searched_number = command
    try:
        del dictionary[searched_number]

    except KeyError:
        print("Number does not exist in dictionary")

    command = input()

print(dictionary)
