user_name = input()
data = input()

while not data == "Sign up":
    data = data.split()
    command = data[0]

    if command == "Case":
        case = data[1]
        if case == "lower":
            user_name = user_name.lower()
            print(user_name)
        else:
            user_name = user_name.upper()
            print(user_name)

    elif command == "Reverse":
        start_index = int(data[1])
        end_index = int(data[2])
        current_string = ""
        if start_index <= len(user_name) - 1 and end_index <= len(user_name) - 1:
            current_string = user_name[start_index:end_index + 1]
            current_string = current_string[::-1]
            print(current_string)

    elif command == "Cut":
        substring = data[1]

        if substring in user_name:
            user_name = user_name.replace(substring, "")
            print(user_name)
        else:
            print(f"The word {user_name} doesn't contain {substring}.")

    elif command == "Replace":
        char_to_replace = data[1]
        user_name = user_name.replace(char_to_replace, "*")
        print(user_name)

    elif command == "Check":
        check_char = data[1]
        if check_char in user_name:
            print("Valid")
        else:
            print(f"Your username must contain {check_char}.")

    data = input()