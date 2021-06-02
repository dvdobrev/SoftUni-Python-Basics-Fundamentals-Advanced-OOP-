data = input()
sides = {}

while not data == "Lumpawaroo":
    splited_data = data.split()
    if "|" in splited_data:
        side = splited_data[0]
        user = splited_data[2]
        if side not in sides:
            sides[side] = []
            if user not in sides.values():
                sides[side].append(user)

    else:
        splited_data.remove("->")
        name = len(splited_data) - 1
        side = ""
        user = []
        for which_side in range(name, len(splited_data)):
            side += splited_data[which_side]

        if len(splited_data) > 2:
            for which_user in range(len(splited_data) - 1):
                user.append(splited_data[which_user])
        else:
            user = splited_data[0]
            side = splited_data[1]
        user = " ".join(user)

        for key, value in sides.items():
            if user in value:
                user = sides.pop(key)
        sides[side].append(user)

    data = input()

print(sides)