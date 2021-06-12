import os

data = input()

while not data == "End":
    data = data.split("-")
    command = data[0]
    file_name = data[1]

    if command == "Create":
        with open(file_name, "w") as file:
            pass

    elif command == "Add":
        content = data[2]
        with open(f"{file_name}", "a") as file:
            file.writelines(content + "\n")

    elif command == "Replace":
        old_string = data[2]
        new_string = data[3]
        text = ""
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                text = file.read()
                if old_string in text:
                    text = text.replace(old_string, new_string)

            with open(file_name, "w") as file:
                file.writelines(text)

        else:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    data = input()
