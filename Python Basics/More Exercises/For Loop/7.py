stadion = int(input())
total_fens = int(input())

sektor_a = 0
sektor_b = 0
sektor_v = 0
sektor_g = 0

for i in range(1,total_fens + 1):
    sektor = input()
    if sektor == 'A':
        sektor_a += 1
    elif sektor == 'B':
        sektor_b += 1
    elif sektor == 'V':
        sektor_v += 1
    elif sektor == 'G':
        sektor_g += 1
perscent_a = sektor_a / total_fens * 100
perscent_b = sektor_b / total_fens * 100
perscent_v = sektor_v / total_fens * 100
perscent_g = sektor_g / total_fens * 100
total_percent = ((sektor_a + sektor_b + sektor_v + sektor_g) / stadion) * 100


print(f'{perscent_a:.2f}%')
print(f'{perscent_b:.2f}%')
print(f'{perscent_v:.2f}%')
print(f'{perscent_g:.2f}%')
print(f'{total_percent:.2f}%')
