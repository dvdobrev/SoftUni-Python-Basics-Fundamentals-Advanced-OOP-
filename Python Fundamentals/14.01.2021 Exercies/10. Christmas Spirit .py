quantity = int(input())
days = int(input())

costs = 0
spirit = 0
days_counter = 0

while days > 0:
    days_counter += 1
    days -= 1
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        costs += quantity * 2
        spirit += 5
    if days_counter % 3 == 0:
        costs += quantity * 8
        spirit += 13
    if days_counter % 5 == 0:
        costs += quantity * 15
        spirit += 17
    if days_counter % 3 == 0 and days_counter % 5 == 0:
        spirit += 30
    if days_counter % 10 == 0:
        spirit -= 20
        costs += 23

    if days_counter % 10 == 0 and days == 0:
        spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {spirit}")




