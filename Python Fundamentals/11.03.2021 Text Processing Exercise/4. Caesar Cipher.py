text = input()

encrypt_text = ""

for char in text:
    current_char = ord(char) + 3
    encrypt_text += chr(current_char)

print(encrypt_text)