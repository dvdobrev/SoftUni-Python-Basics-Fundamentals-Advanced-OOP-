vaucher = int(input())
produkt_name = input()

ticket_counter = 0
others = 0

while produkt_name != 'End':
    if len(produkt_name) > 8:
        vaucher -= ord(produkt_name[0])
        vaucher -= ord(produkt_name[1])
        if vaucher < 0:
            break
        else:
            ticket_counter += 1
    else:
        vaucher -= ord(produkt_name[0])
        if vaucher < 0:
            break
        else:
            others += 1

    produkt_name = input()

print(f'{ticket_counter}')
print(f'{others}')
