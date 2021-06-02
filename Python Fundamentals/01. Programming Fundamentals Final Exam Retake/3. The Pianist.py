n = int(input())
pieces = {}

for num in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "Key": key}

data = input()

while not data == "Stop":
    data = data.split("|")
    command = data[0]
    if command == "Add":
        piece, composer, key = data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        piece = data[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece = data[1]
        new_key = data[2]
        if piece in pieces:
            pieces[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    data = input()

pieces = sorted(pieces.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))

for el in pieces:
    print(f"{el[0]} -> Composer: {el[1]['composer']}, Key: {el[1]['Key']}")