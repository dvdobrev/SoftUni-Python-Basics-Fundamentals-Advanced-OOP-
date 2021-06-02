number1 = int(input())
number2 = int(input())
magic_number = int(input())
counter = 0
is_found = False

for x1 in range(number1, number2 + 1):
    for x2 in range(number1, number2 + 1):
        counter += 1
        if x1 + x2 == magic_number:
            is_found = True
            print(f'Combination N:{counter} ({x1} + {x2} = {magic_number})')
            break
    if is_found:
        break

if not is_found:
    print(f'{counter} combinations - neither equals {magic_number}')