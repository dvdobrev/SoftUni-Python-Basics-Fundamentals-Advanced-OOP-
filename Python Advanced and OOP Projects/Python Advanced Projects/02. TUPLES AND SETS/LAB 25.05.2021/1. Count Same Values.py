text = [float(el) for el in input().split(" ")]

values_count = {}

for el in text:
    if el not in values_count:
        values_count[el] = 0
    values_count[el] += 1

for value, count in values_count.items():
    print(f"{value} - {count} times")