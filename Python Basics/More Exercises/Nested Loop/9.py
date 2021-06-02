n1 = int(input()) # начало на интервал
n2 = int(input())  # край на интервал
magic_number = int(input())
counter = 0
found = False

for i1 in range(n1, n2 + 1):
    if found == False:
        for i2 in range(n1, n2 + 1):
            if i1 + i2 == magic_number:
                counter += 1
                found = True
                print(f'Combination N:{counter} ({i1} + {i2} = {magic_number})')
                break

            else:
                counter += 1
if found == False:
    print(f'{counter} combinations - neither equals {magic_number}')

