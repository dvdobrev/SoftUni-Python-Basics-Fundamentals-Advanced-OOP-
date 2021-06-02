concealed_message = input()
instructions = input()
# ChangeAll
# InsertSpace:|:5
while not instructions == "Reveal":
    instructions = instructions.split(":|:")
    if instructions[0] == "InsertSpace":
        index_to_insert = int(instructions[1])
        concealed_message = concealed_message[:index_to_insert] + " " + concealed_message[index_to_insert:]
        print(concealed_message)
    elif instructions[0] == "Reverse":
        substring_to_cut = instructions[1]
        if substring_to_cut in concealed_message:
            substring_index = concealed_message.find(substring_to_cut)
            cutted_subtring = concealed_message[substring_index:substring_index + len(substring_to_cut)]
            reversed_cutted_substring = cutted_subtring[::-1]
            concealed_message = concealed_message[:substring_index] + concealed_message[substring_index + len(substring_to_cut):] + reversed_cutted_substring
            print(concealed_message)
        else:
            print("error")

    elif instructions[0] == "ChangeAll":
        substring_to_be_changed = instructions[1]
        substring_to_insert = instructions[2]
        if substring_to_be_changed in concealed_message:
            concealed_message = concealed_message.replace(substring_to_be_changed, substring_to_insert)
            print(concealed_message)

    instructions = input()

print(f"You have a new text message: {concealed_message}")