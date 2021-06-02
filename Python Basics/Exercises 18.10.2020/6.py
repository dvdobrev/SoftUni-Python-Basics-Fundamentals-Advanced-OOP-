N1 = int(input())
N2 = int(input())
operator = input() #"+", "-", "*", "/", "%".

result = 0
even_odd = ''

if operator == '+':
    result = N1 + N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')

elif operator == '-':
    result = N1 - N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')

elif operator == '*':
    result = N1 * N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {even_odd}')

elif operator == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")

elif operator == '%':
    if N1 == 0:
        print(f"Cannot divide {N2} by zero")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
