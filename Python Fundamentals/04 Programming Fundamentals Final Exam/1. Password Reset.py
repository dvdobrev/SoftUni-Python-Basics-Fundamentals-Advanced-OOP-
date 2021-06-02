password = input()
data = input()

while not data == "Done":
    data = data.split()
    command = data[0]

    if command == "TakeOdd":
        current_password = ""
        for el in range(1, len(password), 2):
            current_password += password[el]
        password = current_password
        print(password)

    elif command == "Cut":
        start_index = int(data[1])
        length = int(data[2])
        password = password[:start_index] + password[start_index + length:]
        print(password)

    elif command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")

    data = input()

print(f"Your password is: {password}")