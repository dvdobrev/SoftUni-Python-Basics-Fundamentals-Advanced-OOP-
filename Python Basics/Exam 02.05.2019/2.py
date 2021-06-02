budget = float(input())
benzin_needed = float(input())
day = input()
safari_price = 0

if day == 'Saturday':
    safari_price += (100 + (2.10 * benzin_needed)) * 0.9

elif day == 'Sunday':
    safari_price += (100 + (2.10 * benzin_needed)) * 0.8

if safari_price <= budget:
    print(f'Safari time! Money left: {budget - safari_price:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {safari_price - budget:.2f} lv.')