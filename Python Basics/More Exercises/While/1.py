detergent = int(input()) * 750
command = input()
cleaned_dishes = 0
cleaned_pots = 0
counter = 1
enougth = True

while command != 'End':
    plates = int(command)
    if counter % 3 == 0:
        cleaned_pots += plates
        detergent -= plates * 15
        counter += 1
    else:
        cleaned_dishes += plates
        detergent -= plates * 5
        counter += 1

    if detergent >= 0:
         command = input()

    else:
        enougth = False
        print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
        break


if enougth:
    print('Detergent was enough!')
    print(f'{cleaned_dishes} dishes and {cleaned_pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')


