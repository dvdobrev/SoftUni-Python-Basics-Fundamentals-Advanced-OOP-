n = int(input())
couples = n * 2
couples1 = 0
couples2 = 0
couples3 = 0
couples4 = 0
couples5 = 0

for i in range(1,couples + 1):
    number = int(input())
    if i == 1 or i == 2:
        couples1 += number
    elif i == 3 or i == 4:
        couples2 += number
    elif i == 5 or i == 6:
        couples3 += number
    elif i == 7 or i == 8:
        couples4 += number
    elif i == 9 or i == 10:
        couples5 += number

dif1 = abs(couples1 - couples2)
if dif1 == 0:
    dif1 = couples1

dif2 = abs(couples2 - couples3)
if dif2 == 0:
    dif2 = couples2
dif3 = abs(couples3 - couples4)
if dif3 == 0:
    dif3 = couples3
dif4 = abs(couples4 - couples5)
if dif4 == 0:
    dif4 = couples4
max = 0
yes = (couples1 + couples2 + couples3 + couples4 + couples5) / n
if dif1 > dif2:
    max = dif1
else:
    max = dif2
if dif2 > dif3:
    max = dif2
else:
    max = dif3
if dif3 > dif4:
    max = dif3
else:
    max = dif4

if yes == n or yes % 2 == 0:
    print(f'Yes, value = {couples1}')
else:
    print(f'No, maxdiff = {max}')