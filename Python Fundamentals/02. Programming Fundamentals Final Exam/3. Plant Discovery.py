n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant] = {"rarity": rarity, "rating": [], "average": 0}

data = input()

while not data == "Exhibition":
    data = data.split(": ")
    command = data[0]
    if command == "Rate":
        plant, rating = data[1].split(" - ")
        if plant in plants:
            rating = int(rating)
            plants[plant]["rating"].append(rating)
        else:
            print("error")

    elif command == "Update":
        plant, new_rarity = data[1].split(" - ")
        if plant in plants:
            plants[plant]["rarity"] = int(new_rarity)
        else:
            print("error")

    elif command == "Reset":
        plant = data[1]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

    data = input()

for k, v in plants.items():
    if not (plants[k]["rating"]) == []:
        average = sum(plants[k]["rating"]) / len((plants[k]["rating"]))
        plants[k]["average"] = float(average)

plants = dict(sorted(plants.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["average"])))

print("Plants for the exhibition:")

for a, b in plants.items():
    avg = plants[a]["average"]
    print(f"- {a}; Rarity: {plants[a]['rarity']}; Rating: {avg:.2f}")