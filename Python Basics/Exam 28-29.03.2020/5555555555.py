capasity = float(input())
command = input()
total_suitcases = 0
enougth = True

while command != 'End':
    command = float(command)
    if command >= capasity:
        print(f'No more space!')
        enougth = False
        break
    total_suitcases += 1
    if total_suitcases % 3 == 0:
        capasity -= command + (command * 0.1)
    else:
        capasity -= command
    command = input()
if enougth:
    print(f'Congratulations! All suitcases are loaded!')
print(f'Statistic: {total_suitcases} suitcases loaded.')