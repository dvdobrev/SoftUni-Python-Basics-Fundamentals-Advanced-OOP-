import os

data = input()

while not data == "End":
    data = data.split("-")
    command = data[0]
    file_name = data[1]

    if command == "Create":
        with open(f"{file_name}", "w") as file:
            pass

    elif command == "Add":
        content = data[2]
        with open(f"{file_name}", "a") as file:
            file.writelines(f"{(content)}\n")

    elif command == "Replace":
        old_string = data[2]
        new_string = data[3]
        if os.path.exists(file_name):
            with open(f"{file_name}", "r+") as file:
                text = [el[:-1] for el in file.readlines()]
                new_text = []
                for el in text:
                    if old_string in el:
                        el = el.replace(old_string, new_string)
                    new_text.append(el)
                new_text = "\n".join([word for word in new_text])
                file.seek(0)
                file.writelines(new_text)

        else:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    data = input()