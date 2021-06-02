import  math

shirina = float(input())
daljina = float(input())
visochina = float(input())
sredna_visochina_astronavti = float(input())
visochina_na_staqta = sredna_visochina_astronavti + 0.4

atronavt_counter = 0

obem_na_koraba = shirina * daljina * visochina
room = 2 * 2 * visochina_na_staqta

broi_stai = obem_na_koraba / room

if 3 <= broi_stai <= 10:
    print(f'The spacecraft holds {math.floor(broi_stai)} astronauts.')
elif broi_stai < 3:
    print('The spacecraft is too small.')
elif broi_stai > 10:
    print('The spacecraft is too big.')
