names = {name: [] for name in input().split(", ")}

command = input()

while not command == "End":
    hero, item, price = command.split("-")
    if item not in names[hero]:
        names[hero] += [item, price]

    command = input()

for hero, items in names.items():
    price = [int(item) for item in items if item.isdecimal()]
    print(f"{hero} -> Items: {int(len(items) / 2)}, Cost: {sum(price)}")