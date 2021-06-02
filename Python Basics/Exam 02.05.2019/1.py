chiken = int(input())
fish = int(input())
vegi = int(input())

total_chiken = chiken * 10.35
total_fish = fish * 12.40
total_vegi = vegi * 8.15
total_price = total_chiken + total_fish + total_vegi
desert = total_price * 0.2
total = total_price + desert + 2.5

print(f'Total: {total:.2f}')