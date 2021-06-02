number = float(input())
vhod = input()
izhod = input()

mm = 1
cm = mm * 10
m = cm * 100

if vhod == 'mm':
    if izhod == 'cm':
        rezult = number / 10
        print(f'{rezult:.3f}')
    elif izhod == 'm':
        rezult = number / 1000
        print(f'{rezult:.3f}')
elif vhod == 'cm':
    if izhod == 'mm':
        rezult = number * 10
        print(f'{rezult:.3f}')
    elif izhod == 'm':
        result = number / 100
        print(f'{result:.3f}')
elif vhod == 'm':
    if izhod == 'cm':
        result = number * 100
        print(f'{result:.3f}')
    elif izhod == 'mm':
        result = number * 1000
        print(f'{result:.3f}')
