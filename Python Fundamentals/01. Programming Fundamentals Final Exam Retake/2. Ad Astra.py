import re

text = input()

valid_foods_pattern = r"(\||#)[a-zA-z\s]+\1[0-9]{2}/[0-9]{2}/[0-9]{2}\1[0-9]+\1"

valid_foods = [el.group() for el in re.finditer(valid_foods_pattern, text)]
valid_foods_as_string = ""
for el in valid_foods:
    valid_foods_as_string += el

foods_pattern = r"[A-Za-z\s]+"
foods = [el.group() for el in re.finditer(foods_pattern, valid_foods_as_string)]

expiration_date_pattern = r"[0-9]{2}/[0-9]{2}/[0-9]{2}"
expiration_date = [el.group() for el in re.finditer(expiration_date_pattern, valid_foods_as_string)]

calories_pattern = r"(?<=(#|\|))\d+(?=\1)"
calories = [int(el.group()) for el in re.finditer(calories_pattern, valid_foods_as_string)]

total_calories = sum(calories)

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for el in range(len(foods)):
    print(f"Item: {foods[el]}, Best before: {expiration_date[el]}, Nutrition: {calories[el]}")
