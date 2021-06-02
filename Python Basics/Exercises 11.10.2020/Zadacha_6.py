budget = float(input())
statisti = int(input())
dekor = budget * 0.1
cena_obleklo = float(input())
razhodi_za_obleklo = statisti * cena_obleklo
razhodi = razhodi_za_obleklo + dekor

if statisti > 150:
    otstupka = razhodi_za_obleklo * 0.1
    kraina_cena_obleklo = razhodi_za_obleklo - otstupka
    razhodi = kraina_cena_obleklo + dekor
    ostatuk = budget - razhodi
    izlishak = abs(razhodi - budget)
    if ostatuk >= 0:
        print('Action!')
        print(f'Wingard starts filming with {ostatuk:.2f} leva left.')
    else:
        print(f'Not enough money!')
        print(f'Wingard needs {izlishak:.2f} leva more.')

else:
    ostatuk = budget - razhodi
    izlishak = abs(razhodi - budget)
    if ostatuk >= 0:
        print('Action!')
        print(f'Wingard starts filming with {ostatuk:.2f} leva left.')
    else:
        print(f'Not enough money!')
        print(f'Wingard needs {izlishak:.2f} leva more.')
