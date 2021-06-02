import math

form = input()


if form == 'square':
    a = float(input())
    lice = a * a
    print(f'{lice:.3f}')

elif form == 'rectangle':
    width = float(input())
    high = float(input())
    lice_r = width * high
    print(f'{lice_r:.3f}')


elif form == 'circle':
    razmer_c = float(input())
    lice_c = razmer_c * razmer_c * math.pi
    print(f'{lice_c:.3f}')

elif form == 'triangle':
    razmer_a = float(input())
    razmer_b = float(input())
    lice_t = razmer_a * razmer_b / 2
    print(f'{lice_t:.3f}')


