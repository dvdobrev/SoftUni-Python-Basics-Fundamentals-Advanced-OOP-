import sys
n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    elif i % 2 != 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize and odd_max == -sys.maxsize or odd_min == 0:
    print('OddMin=No,')
elif odd_min == sys.maxsize:
    odd_min = odd_max
    print(f'OddMin={odd_min:.2f},')
else:
    print(f'OddMin={odd_min:.2f},')


if odd_min == sys.maxsize and odd_max == -sys.maxsize or odd_max == 0:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')


print(f'EvenSum={even_sum:.2f},')

if even_min == sys.maxsize and even_max == -sys.maxsize or even_min == 0:
    print('EvenMin=No,')
elif even_min == sys.maxsize:
    even_min = even_max
    print(f'EvenMin={even_min:.2f},')
else:
    print(f'EvenMin={even_min:.2f},')


if even_min == sys.maxsize and even_max == -sys.maxsize or even_max == 0:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')