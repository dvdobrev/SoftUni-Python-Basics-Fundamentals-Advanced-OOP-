import re

text = input()

pattern = r"www.[a-zA-Z0-9-]+(\.[a-z]+)+"

while not text == "":
    valid_emails = [el.group() for el in re.finditer(pattern, text)]
    if valid_emails:
        print(*valid_emails)
    text = input()