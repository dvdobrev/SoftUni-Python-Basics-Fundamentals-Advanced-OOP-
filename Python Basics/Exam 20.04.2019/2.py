import math
guest = int(input())
buedget = int(input())

needed_kosunak = math.ceil(guest / 3)
needed_eggs = guest * 2
price_kosunak = needed_kosunak * 4
price_eggs = needed_eggs * 0.45
total_costs = price_kosunak + price_eggs

if buedget >= total_costs:
    print(f'Lyubo bought {needed_kosunak} Easter bread and {needed_eggs} eggs.')
    print(f'He has {buedget - total_costs:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {total_costs - buedget:.2f} lv. more.')