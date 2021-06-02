import re

text = input()
numbers = ""
emojis = []
cool_emojis = []

for num in range(len(text)):
    if text[num].isnumeric():
        numbers += text[num]

cool_threshold = 1
for num in numbers:
    num = int(num)
    cool_threshold *= num

pattern = r"(\*\*|::)[A-Z][a-z][a-z]+\1"

valid_patterns = [el.group() for el in re.finditer(pattern, text)]

for el in valid_patterns:
    word = el[2:-2]
    current_threshold = 0
    for num in range(len(word)):
        current_threshold += ord(word[num])
    if current_threshold >= cool_threshold:
        cool_emojis.append(el)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_patterns)} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")