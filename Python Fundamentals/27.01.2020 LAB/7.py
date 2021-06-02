lisf_of_gifts = input().split()
command = input()  # OutOfSrock Eggs

while not command == "No Money":
    current_command = command.split()
    current_gift = current_command[1]

    if current_command[0] == "OutOfStock":
        for index in range(len(lisf_of_gifts)):
            if lisf_of_gifts[index] == current_gift:
                lisf_of_gifts[index] = "None"

    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index < len(lisf_of_gifts):
            lisf_of_gifts[index] = current_gift

    elif current_command[0] == "JustInCase":
        lisf_of_gifts[-1] = current_gift

    command = input()

for gift in lisf_of_gifts:
    if not gift == "None":
        print(gift, end=" ")





