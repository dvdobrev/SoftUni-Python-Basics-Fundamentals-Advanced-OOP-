target = float(input())
cocktail_name = input()
earned_money = 0
enought = False


while cocktail_name != 'Party!':
    cocktail_quantity = int(input())
    cockail_price = len(cocktail_name)
    order_price = cockail_price * cocktail_quantity
    if order_price % 2 != 0:
        order_price = order_price * 0.75
        earned_money += order_price
    else:
        earned_money += order_price
    if earned_money >= target:
        enought = True
        print('Target acquired.')
        break

    cocktail_name = input()


if enought == False:
    print(f'We need {target - earned_money:.2f} leva more.')

print(f'Club income - {earned_money:.2f} leva.')