eggs = int(input())
command = input()
#buy_eggs = 0
#fill_eggs = 0
sell_eggs = 0
more = True

while command != 'Close':
    eggs_quantity = int(input())
    if command == 'Buy':
        if eggs_quantity > eggs:
            more = False
            print(f'Not enough eggs in store!\nYou can buy only {eggs}.')
            break
        eggs -= eggs_quantity
        sell_eggs += eggs_quantity
    elif command == 'Fill':
        eggs += eggs_quantity
    command = input()

if more:
    print(f'Store is closed!\n{sell_eggs} eggs sold.')
