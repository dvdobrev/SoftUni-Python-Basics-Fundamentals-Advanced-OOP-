key_numbers = [int(el) for el in input().split()]
text = input()
hidden_message = ""
type = ""
coordinates = ""
type_index = []
coordinates_index = []

while not text == "find":
    text_as_ascii = [ord(el) for el in text]
    text_length = len(text_as_ascii)
    key_index = 0
    text_index = 0
    while not text_length == text_index:
        if key_index > len(key_numbers) - 1:
            key_index = 0

        hidden_message += chr(text_as_ascii[text_index] - (key_numbers[key_index]))
        key_index += 1
        text_index += 1

    for char in range(len(hidden_message)):
        if hidden_message[char] == "&":
            type_index.append(char)
    for char in range(len(hidden_message)):
        if hidden_message[char] == '<' or hidden_message[char] == '>':
            coordinates_index.append(char)
    type = hidden_message[type_index[0] + 1:type_index[1]]
    coordinates = hidden_message[coordinates_index[0] + 1: -1]

    print(f"Found {type} at {coordinates}")
    hidden_message = ""
    type = ""
    coordinates = ""
    type_index = []
    coordinates_index = []

    text = input()