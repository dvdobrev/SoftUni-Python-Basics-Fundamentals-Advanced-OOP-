size = input()
color = input()
quantity = int(input())
price = 0

if size == 'Large':
    if color == 'Red':
        price = 16
    elif color == 'Green':
        price = 12
    elif color == 'Yellow':
        price = 9
elif size == 'Medium':
    if color == 'Red':
        price = 13
    elif color == 'Green':
        price = 9
    elif color == 'Yellow':
        price = 7
elif size == 'Small':
    if color == 'Red':
        price = 9
    elif color == 'Green':
        price = 8
    elif color == 'Yellow':
        price = 5

eggs_price = quantity * price
costs = eggs_price * 0.35
money_left = eggs_price - costs

print(f'{money_left:.2f} leva.')


