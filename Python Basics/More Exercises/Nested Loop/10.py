coins1_quantity = int(input())
coins2_quantity = int(input())
banknote_quantity = int(input())
sum = int(input())

for c1 in range(coins1_quantity + 1):
    for c2 in range(coins2_quantity + 1):
        for b1 in range(banknote_quantity + 1):
            if c1 + (c2 * 2) + (b1 * 5) == sum:
                print(f'{c1} * 1 lv. + {c2} * 2 lv. + {b1} * 5 lv. = {sum} lv.')


