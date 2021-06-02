from collections import deque

END_COMMAND = "End"
REFILL_COMMAND = "refill"

people = deque()
total_liters = int(input())

command = input()

while not command == "Start":
    people.append(command)

    command = input()

command = input()

while not command == END_COMMAND:
    if command.startswith("refill"):
        command = command.split()
        liters_to_refill = int(command[1])
        total_liters += liters_to_refill
    else:
        water_to_take = int(command)
        if total_liters >= water_to_take:
            print(f"{people.popleft()} got water")
            total_liters -= water_to_take
        else:
            print(f"{people.popleft()} must wait")

    command = input()

print(f"{total_liters} liters left")