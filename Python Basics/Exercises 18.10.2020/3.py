type_flower = input()  #"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
quantity_flower = int(input())
budget = int(input())

price = 0

if type_flower == 'Roses':
    price = 5
    if quantity_flower > 80:
        price -= price * 0.10
elif type_flower == 'Dahlias':
    price = 3.80
    if quantity_flower > 90:
        price -= price * 0.15
elif type_flower == 'Tulips':
    price = 2.80
    if quantity_flower > 80:
        price -= price * 0.15
elif type_flower == 'Narcissus':
    price = 3
    if quantity_flower < 120:
        price += price * 0.15
elif type_flower == 'Gladiolus':
    price = 2.50
    if quantity_flower < 80:
        price += price * 0.20

money_needed = quantity_flower * price
diff = abs(budget - money_needed)

if budget >= money_needed:
    print(f'Hey, you have a great garden with {quantity_flower} {type_flower} and {diff:.2f} leva left.')
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")