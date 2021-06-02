text = input()

data = input()

while not data == "Decode":
    data = data.split("|")
    command = data[0]
    if command == "Move":
        letters_amount_to_move = int(data[1])
        cuted_letters = ""
        cuted_letters += text[:letters_amount_to_move]
        text = text[letters_amount_to_move:] + cuted_letters

    elif command == "Insert":
        index = int(data[1])
        value = data[2]
        text = text[:index] + value + text[index:]

    elif command == "ChangeAll":
        substring_to_change = data[1]
        new_substring = data[2]
        text = text.replace(substring_to_change, new_substring)

    data = input()

print(f"The decrypted message is: {text}")