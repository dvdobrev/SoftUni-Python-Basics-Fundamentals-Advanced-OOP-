type_of_projektion = input()
#r = red
#c = coloni
r = int(input())
c = int(input())

tickets = r * c


Premiere = 12.00
Normal = 7.50
Discount = 5.00


if type_of_projektion == 'Premiere':
    tickets = tickets * Premiere
    print(f'{tickets:.2f} leva')

elif type_of_projektion == 'Normal':
    tickets = tickets * Normal
    print(f'{tickets:.2f} leva')

elif type_of_projektion == 'Discount':
    tickets = tickets * Discount
    print(f'{tickets:.2f} leva')
