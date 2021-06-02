import re

text = input()
pattern = r"\d+"
all_numbers = []

while not text == "":
    numbers = re.findall(pattern, text)
    all_numbers.extend(numbers)
    text = input()

print(*all_numbers)