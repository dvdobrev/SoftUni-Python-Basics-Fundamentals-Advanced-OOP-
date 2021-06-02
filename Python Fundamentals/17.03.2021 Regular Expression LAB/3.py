import re

text = input()

pattern = r"\b(?P<Day>\d{2})(?P<separator>(.|-|/))(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"
valid_dates = [date.groupdict() for date in re.finditer(pattern, text)]
print('\n'.join([f"Day: {datee['Day']}, Month: {datee['Month']}, Year: {datee['Year']}" for datee in valid_dates]))