def check_if_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False

targets = [int(target) for target in input().split()]
command = input()


while not command == "End":
    command, index, value = command.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if check_if_index_is_valid(index, len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if check_if_index_is_valid(index, len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        left_most_index = index - value
        right_most_index = index + value
        if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(targets)) and check_if_index_is_valid(right_most_index, len(targets)):
            left_unstriked_index = targets[:left_most_index]
            right_unstriked_index = targets[right_most_index+1:]
            targets = left_unstriked_index + right_unstriked_index
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(el) for el in targets]))