term = input()
contrakt_type = input()
internet = input()
months = int(input())
month_price = 0
total_price = 0

if term == 'one':
    if contrakt_type == 'Small':
        month_price = 9.98
        total_price = months * 9.98
    elif contrakt_type == 'Middle':
        month_price = 18.99
        total_price = months * 18.99
    elif contrakt_type == 'Large':
        month_price = 25.98
        total_price = months * 25.98
    elif contrakt_type == 'ExtraLarge':
        month_price = 35.99
        total_price = months * 35.99

elif term == 'two':
    if contrakt_type == 'Small':
        month_price = 8.58
        total_price = months * 8.58
    elif contrakt_type == 'Middle':
        month_price = 17.09
        total_price = months * 17.09
    elif contrakt_type == 'Large':
        month_price = 23.59
        total_price = months * 23.59
    elif contrakt_type == 'ExtraLarge':
        month_price = 31.79
        total_price = months * 31.79

if internet == 'yes':
    if month_price <= 10:
        month_price += 5.50
    elif 10 < month_price <= 30:
        month_price += 4.35
    elif month_price > 30:
        month_price += 3.85
    total_price = month_price * months

if term == 'two':
    total_price = total_price * 0.9625

print(f'{total_price:.2f} lv.')
