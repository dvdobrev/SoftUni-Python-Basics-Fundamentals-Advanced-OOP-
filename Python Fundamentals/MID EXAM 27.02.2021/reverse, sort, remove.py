colection = [int(el) for el in input().split()]

command = input()
left_list = []
right_list = []
current_list = []
new_collection = []
current_list_2 = []

while not command == "end":
    command = command.split()
    if command[0] == "reverse":
        start = int(command[2])
        count = int(command[4])
        left_list = colection[:start]
        right_list = colection[(start + count):]
        current_list = colection[start:(start + count)]
        current_list_2 = list(reversed(current_list))
        new_collection = left_list + current_list_2 + right_list

    elif command[0] == "sort":
        start = int(command[2])
        count = int(command[4])
        left_list = colection[:start]
        right_list = colection[(start + count):]
        current_list = colection[start:(start + count)]
        current_list_2 = list(sorted(current_list))
        new_collection = left_list + current_list_2 + right_list

    elif command[0] == "remove":
        start = int(command[1])
        left_list = colection[:start]
        new_collection = colection[len(left_list):]

    command = input()

print(left_list)
print(right_list)
print(current_list)
print(current_list_2)
print(new_collection)
print(*new_collection, sep=", ")