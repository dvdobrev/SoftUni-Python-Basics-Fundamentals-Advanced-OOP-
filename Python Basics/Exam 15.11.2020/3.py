team = input()
suvenir = input()
suvenir_quantity = int(input())
suvenir_price = 0
suvenir_counter = 0


if team == 'Argentina':
    if suvenir == 'flags':
        suvenir_price += 3.25 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'caps':
        suvenir_price += 7.20 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'posters':
        suvenir_price += 5.10 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'stickers':
        suvenir_price += 1.25 * suvenir_quantity
        suvenir_counter += 1

elif team == 'Brazil':
    if suvenir == 'flags':
        suvenir_price += 4.20 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'caps':
        suvenir_price += 8.50 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'posters':
        suvenir_price += 5.35 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'stickers':
        suvenir_price += 1.20 * suvenir_quantity
        suvenir_counter += 1

elif team == 'Croatia':
    if suvenir == 'flags':
        suvenir_price += 2.75 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'caps':
        suvenir_price += 6.90 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'posters':
        suvenir_price += 4.95 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'stickers':
        suvenir_price += 1.10 * suvenir_quantity
        suvenir_counter += 1

elif team == 'Denmark':
    if suvenir == 'flags':
        suvenir_price += 3.10 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'caps':
        suvenir_price += 6.50 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'posters':
        suvenir_price += 4.80 * suvenir_quantity
        suvenir_counter += 1
    elif suvenir == 'stickers':
        suvenir_price += 0.90 * suvenir_quantity
        suvenir_counter += 1

if team != 'Argentina' and team != 'Brazil' and team != 'Croatia' and team != 'Denmark':
    print('Invalid country!')
elif suvenir != 'flags' and suvenir != 'caps' and suvenir != 'posters' and suvenir != 'stickers':
    print('Invalid stock!')
else:
    print(f'Pepi bought {suvenir_quantity} {suvenir} of {team} for {suvenir_price:.2f} lv.')