name_list = input().split(", ")
command = input()
blacklisted_count = 0
lost_count = 0
current_list = name_list

while not command == "Report":
    command = command.split()
    if command[0] == "Blacklist":
        name = command[1]
        if name in name_list:
            name_list = [n.replace(f"{name}", "Blacklisted")for n in name_list]
            blacklisted_count += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        username = name_list[index]
        if username == "Blacklisted" or username == "Lost":
            pass
        else:
            name_list = [n.replace(f"{username}", "Lost")for n in name_list]
            lost_count += 1
            print(f"{username} was lost due to an error.")

    elif command[0] == "Change":
        index = int(command[1])
        if index <= len(name_list):
            new_name = command[2]
            username = name_list[index]
            name_list[index] = new_name
            print(f"{username} changed his username to {new_name}. ")

    command = input()
print(f"Blacklisted names: {blacklisted_count} ")
print(f"Lost names: {lost_count} ")
print(" ".join(name_list))

# Mike, John, Eddie
# Blacklist Mike
# Error 0
# Error 1
# Change 2 Mike123
# Report