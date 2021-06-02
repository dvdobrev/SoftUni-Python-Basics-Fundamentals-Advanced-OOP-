activation_key = input()
command = input()

while not command == "Generate":
    current_command = command.split(">>>")
    if current_command[0] == "Contains":
        if current_command[1] in activation_key:
            print(f"{activation_key} contains {current_command[1]}")
        else:
            print("Substring not found!")
    elif current_command[0] == "Flip":
        upper_or_lower = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        first_string = ""
        changed_string = ""
        last_string = ""
        if upper_or_lower == "Upper":
            first_string = activation_key[:start_index]
            changed_string = activation_key[start_index:end_index].upper()
            last_string = activation_key[end_index:]
            activation_key = first_string + changed_string + last_string
            print(activation_key)
        else:
            first_string = activation_key[:start_index]
            changed_string = activation_key[start_index:end_index].lower()
            last_string = activation_key[end_index:]
            activation_key = first_string + changed_string + last_string
            print(activation_key)

    elif current_command[0] == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")