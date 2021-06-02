import re

n = int(input())

valid_text = []
valid_text_as_string = ""
valid_username = []
valid_password = []
counter = 0

pattern = r"([U][$])[A-Z][a-z][a-z]+\1([P][@][$])[A-Za-z]{5,}[0-9]+\2"
pattern_username = r"[A-Z][a-z][a-z]+"
pattern_password = r"[A-Za-z]{5,}[0-9]+"

for el in range(n):
    text = input()
    match = re.match(pattern,text)
    if match:
        valid_text = [el.group() for el in re.finditer(pattern, text)]
        valid_text_as_string = "".join(valid_text)
        valid_username = [el.group() for el in re.finditer(pattern_username, valid_text_as_string)]
        valid_password = [el.group() for el in re.finditer(pattern_password, valid_text_as_string)]
        valid_username = "".join(valid_username)
        valid_password = "".join(valid_password)

        print(f"Registration was successful")
        print(f"Username: {(valid_username)}, Password: {valid_password}")
        counter += 1
        valid_text = []
        valid_text_as_string = ""
        valid_username = []
        valid_password = []
    else:
        print(f"Invalid username or password")

print(f"Successful registrations: {counter}")