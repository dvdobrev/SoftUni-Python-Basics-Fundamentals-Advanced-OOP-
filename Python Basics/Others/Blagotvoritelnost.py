dni = int(input())
sladkari = int(input())
torti = int(input())
gofreti = int(input())
palachinki = int(input())

torta = 45
gofreta = 5.80
palachinka = 3.20

total_torti = torti * sladkari * dni
total_gofreti = gofreti * sladkari * dni
total_palachinki = palachinki * sladkari * dni

suma_torti = torta * total_torti
suma_gofreta = gofreta * total_gofreti
suma_palachinka = palachinka * total_palachinki

total_suma = suma_torti + suma_gofreta + suma_palachinka
razhodi = total_suma / 8
suma_za_blagotvoritelnost = total_suma - razhodi
print (suma_za_blagotvoritelnost)