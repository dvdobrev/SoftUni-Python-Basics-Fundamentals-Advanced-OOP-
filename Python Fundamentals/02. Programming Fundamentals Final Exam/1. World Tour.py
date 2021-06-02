destination = input()

data = input()

while not data == "Travel":
    data = data.split(":")
    command = data[0]

    if command == "Add Stop":
        index = int(data[1])
        string = data[2]
        if index <= len(destination) - 1:
            destination = destination[:index] + string + destination[index:]
        print(destination)

    elif command == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index <= len(destination) - 1 and end_index <= len(destination) - 1:
            destination = destination[:start_index] + destination[end_index + 1:]
        print(destination)

    elif command == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in destination:
            destination = destination.replace(old_string, new_string)
        print(destination)

    data = input()

print(f"Ready for world tour! Planned stops: {destination}")