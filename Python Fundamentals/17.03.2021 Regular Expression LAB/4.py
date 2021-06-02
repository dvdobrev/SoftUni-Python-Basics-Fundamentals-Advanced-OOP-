import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = [num.group() for num in re.finditer(pattern, text)]

print(*valid_numbers)