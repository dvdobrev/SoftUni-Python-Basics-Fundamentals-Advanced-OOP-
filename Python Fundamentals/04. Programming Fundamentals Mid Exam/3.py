neighboors = [int(el) for el in input().split("@")]
command = input()
last_position = 0

while not command == "Love!":
    index = int(command[1])
    if index > len(neighboors):
        index = 0
    if neighboors[index] == 0:
        print(f"Place {neighboors[index]} has Valentine's day." )

    if index
    neighboors[index] -= 2
    current_
    last_position == command[index]
    command = input()

if neighboors == 0:
    print("Mission was successful.")
