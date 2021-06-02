list_of_targets = [int(targets) for targets in input().split()]
index = input()
shooted_target = 0

while not index == "End":
    index = int(index)
    if index < len(list_of_targets):
        current_target = list_of_targets[index]
        if current_target == -1:
            continue
        else:
            shooted_target += 1
        new_list_of_targets = []
        for value in list_of_targets:

            if value > current_target and not value == -1:
                value -= current_target
                new_list_of_targets.append(value)

            elif value <= current_target and not value == -1:
                value += current_target
                new_list_of_targets.append(value)
            else:
                new_list_of_targets.append(value)
        new_list_of_targets[index] = -1
        list_of_targets = new_list_of_targets

    index = input()
list_of_targets = [str(inte) for inte in list_of_targets]
list_of_targets = " ".join(list_of_targets)
print(f"Shot targets: {shooted_target} -> {list_of_targets}")



