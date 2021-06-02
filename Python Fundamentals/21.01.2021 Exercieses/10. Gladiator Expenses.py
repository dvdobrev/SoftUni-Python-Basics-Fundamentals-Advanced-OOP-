lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
costs = 0
shield_brakes_count = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        costs += helmet_price
    if i % 3 == 0:
        costs += sword_price
    if i % 2 == 0 and i % 3 == 0:
        costs += shield_price
        shield_brakes_count += 1
    if shield_brakes_count % 2 == 0 and not shield_brakes_count == 0:
        costs += armor_price
        shield_brakes_count = 0

print(f"Gladiator expenses: {costs:.2f} aureus")

