command = input()
number = 0
prime_numbers = 0
nonprime_numbers = 0

while command != 'stop':
    number = int(command)
    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1

    if counter == 2:
        prime_numbers += number
    else:
        nonprime_numbers += number
    command = input()
print(f'Sum of all prime numbers is: {prime_numbers}')
print(f'Sum of all non prime numbers is: {nonprime_numbers}')