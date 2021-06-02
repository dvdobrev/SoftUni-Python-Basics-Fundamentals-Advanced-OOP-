import re

text = input()

pattern = r"(^_|(?<=\s_))[a-zA-Z]+\b"

data = [el.group() for el in re.finditer(pattern, text)]

print(",".join(data))