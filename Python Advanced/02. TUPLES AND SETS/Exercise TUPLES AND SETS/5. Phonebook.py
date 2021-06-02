data = input()

phone_book = {}

while not data.isnumeric():
    name, number = data.split("-")
    phone_book[name] = number

    data = input()

data = int(data)

for el in range(data):
    name = input()

    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")

    else:
        print(f"Contact {name} does not exist.")