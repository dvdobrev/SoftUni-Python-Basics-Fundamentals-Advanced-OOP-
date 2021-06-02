command = input()
total = 0

while command != 'NoMoreMoney':
    money = float(command)
    if money <= 0:
        print('Invalid operation!')
        break
    else:
        total += money
        print(f'Increase: {money:.2f}')
    command = input()
print(f'Total: {total:.2f}')