stage = input()
ticket_type = input()
ticket_quantity = int(input())
picture = input()
total_price = 0

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        total_price += ticket_quantity * 55.50
    elif ticket_type == 'Premium':
        total_price += ticket_quantity * 105.20
    elif ticket_type == 'VIP':
        total_price += ticket_quantity * 118.90

elif stage == 'Semi final':
    if ticket_type == 'Standard':
        total_price += ticket_quantity * 75.88
    elif ticket_type == 'Premium':
        total_price += ticket_quantity * 125.22
    elif ticket_type == 'VIP':
        total_price += ticket_quantity * 300.40

elif stage == 'Final':
    if ticket_type == 'Standard':
        total_price += ticket_quantity * 110.10
    elif ticket_type == 'Premium':
        total_price += ticket_quantity * 160.66
    elif ticket_type == 'VIP':
        total_price += ticket_quantity * 400

if picture == 'Y':
    if total_price > 4000:
        total_price -= total_price * 0.25
    elif 2500 < total_price <= 4000:
        total_price = (total_price * 0.9) + (ticket_quantity * 40)
    else:
        total_price = total_price + (ticket_quantity * 40)
elif picture == 'N':
    if total_price > 4000:
        total_price = total_price * 0.75
    elif 2500 < total_price <= 4000:
        total_price = total_price * 0.9
    else:
        total_price = total_price


print(f'{total_price:.2f}')


