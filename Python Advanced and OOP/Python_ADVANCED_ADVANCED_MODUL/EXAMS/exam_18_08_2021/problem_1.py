bee_value = [int(x) for x in input().split(" ")]
nectar = [int(x) for x in input().split(" ")]
commands = [x for x in input().split(" ")]

total_honey = 0

while bee_value and nectar:
    current_bee = bee_value[0]
    current_nectar = nectar[-1]
    current_command = commands[0]

    if current_nectar >= current_bee:

        if current_command == "+":
            total_honey += current_bee + current_nectar
            bee_value.pop(0)
            nectar.pop()
            commands.pop(0)

        elif current_command == "-":
            total_honey += abs(current_bee - current_nectar)
            bee_value.pop(0)
            nectar.pop()
            commands.pop(0)

        elif current_command == "*":
            total_honey += abs(current_bee * current_nectar)
            bee_value.pop(0)
            nectar.pop()
            commands.pop(0)

        elif current_command == "/":
            total_honey += abs(current_bee / current_nectar)
            bee_value.pop(0)
            nectar.pop()
            commands.pop(0)

        # else:
        #     total_honey += abs(current_bee / current_nectar)
        #     bee_value.pop(0)
        #     nectar.pop()
        #     commands.pop(0)

    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")

if bee_value:
    print(f"Bees left: ", end="")
    print(*bee_value, sep=", ")

if nectar:
    print(f"Nectar left: ", end="")
    print(*nectar, sep=", ")
