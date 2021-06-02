sold = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for i in range(1, sold + 1):
    name = input()
    if name == 'Hearthstone':
        Hearthstone += 1
    elif name == 'Fornite':
        Fornite += 1
    elif name == 'Overwatch':
        Overwatch += 1
    else:
        Others += 1

print(f'Hearthstone - {(Hearthstone / sold) * 100:.2f}%')
print(f'Fornite - {(Fornite / sold) * 100:.2f}%')
print(f'Overwatch - {(Overwatch / sold) * 100:.2f}%')
print(f'Others - {(Others / sold) * 100:.2f}%')