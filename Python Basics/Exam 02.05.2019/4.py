budget = float(input())
command = input()
total_price = 0
produkt_counter = 0
yes = True

while command != 'Stop':
    produkt_price = float(input())
    produkt_counter = produkt_counter
    produkt_counter +=1

    if produkt_counter % 3 == 0:
        produkt_price = produkt_price / 2

    if produkt_price > budget:
        print('You don\'t have enough money!')
        print(f'You need {produkt_price - budget:.2f} leva!')
        yes = False
        break

    total_price += produkt_price
    budget -= produkt_price
    command = input()

if yes:
    print(f'You bought {produkt_counter} products for {total_price:.2f} leva.')
