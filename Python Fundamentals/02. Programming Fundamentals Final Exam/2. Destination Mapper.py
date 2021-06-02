import re

text = input()

pattern = r"(?<=(\=|/))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"

valid_text = [el.group() for el in re.finditer(pattern, text)]

travel_points = 0

for el in valid_text:
    travel_points += len(el)

print(f"Destinations: {', '.join(valid_text)}")
print(f"Travel Points: {travel_points}")