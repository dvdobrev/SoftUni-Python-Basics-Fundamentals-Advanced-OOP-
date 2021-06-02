budget = int(input())
season = input() # Spring", "Summer", "Autumn" или "Winter";
count_fisherman = int(input())

price = 0

if season == 'Spring':
    if count_fisherman <= 6:
        price = 3000 - (3000 * 0.10)
    elif 7 <= count_fisherman <= 11:
        price = 3000 - (3000 * 0.15)
    elif count_fisherman >= 12:
        price = 3000 - (3000 * 0.25)

elif season == 'Summer':
    if count_fisherman <= 6:
        price = 4200 - (4200 * 0.10)
    elif 7 <= count_fisherman <= 11:
        price = 4200 - (4200 * 0.15)
    elif count_fisherman >= 12:
        price = 4200 - (4200 * 0.25)

elif season == 'Autumn':
    if count_fisherman <= 6:
        price = 4200 - (4200 * 0.10)
    elif 7 <= count_fisherman <= 11:
        price = 4200 - (4200 * 0.15)
    if count_fisherman >= 12:
        price = 4200 - (4200 * 0.25)

elif season == 'Winter':
    if count_fisherman <= 6:
        price = 2600 - (2600 * 0.10)
    elif 7 <= count_fisherman <= 11:
        price = 2600 - (2600 * 0.15)
    elif count_fisherman >= 12:
        price = 2600 - (2600 * 0.25)

if season != 'Autumn' and count_fisherman % 2 == 0:
    price -= price * 0.05

money_needed = abs(budget - price)

if price <= budget:
    print(f"Yes! You have {money_needed:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva.")