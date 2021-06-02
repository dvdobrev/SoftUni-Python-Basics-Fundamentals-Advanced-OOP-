produkts = input().split("!")
data = input()

while not data == "Go Shopping!":
    new_data = data.split()
    command = new_data[0]
    item = new_data[1]
    if command == "Urgent":
        if not item in produkts:
            produkts.insert(0, item)

    elif command == "Unnecessary":
        if item in produkts:
            produkts.remove(item)
    elif command == "Correct":
        if item in produkts:
            produkts = [new.replace(item, new_data[2]) for new in produkts]

    elif command == "Rearrange":
        if item in produkts:
            produkts.remove(item)
            produkts.append(item)

    data = input()

print(", ".join(produkts))