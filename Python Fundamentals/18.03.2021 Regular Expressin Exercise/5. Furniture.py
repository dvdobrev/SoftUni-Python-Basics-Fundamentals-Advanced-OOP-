import re

text = input()
pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)(\s|$)"
names = []
total_money = 0

while not text == "Purchase":
    match = re.match(pattern, text)
    if match:
        data = match.groupdict()
        names.append(data["name"])
        total_money += int(data["quantity"]) * float(data["price"])

    text = input()

print("Bought furniture:")
if names:
    print("\n".join(names))
print(f"Total money spend: {total_money:.2f}")