turns = int(input())
points = 0
count_number1 = 0
count_number2 = 0
count_number3 = 0
count_number4 = 0
count_number5 = 0
count_number6 = 0

for i in range(1, turns + 1):
    number = int(input())
    if 0 <= number <= 9:
        points += number * 0.2
        count_number1 += 1
    elif 10 <= number <= 19:
        points += number * 0.3
        count_number2 += 1
    elif 20 <= number <= 29:
        points += number * 0.4
        count_number3 += 1
    elif 30 <= number <= 39:
        points += 50
        count_number4 += 1
    elif 40 <= number <= 50:
        points += 100
        count_number5 += 1
    elif number < 0 or number > 50:
        points = points / 2
        count_number6 += 1

print(f'{points:.2f}')
print(f'From 0 to 9: {(count_number1 / turns * 100):.2f}%')
print(f'From 10 to 19: {(count_number2 / turns * 100):.2f}%')
print(f'From 20 to 29: {(count_number3 / turns * 100):.2f}%')
print(f'From 30 to 39: {(count_number4 / turns * 100):.2f}%')
print(f'From 40 to 50: {(count_number5 / turns * 100):.2f}%')
print(f'Invalid numbers: {(count_number6 / turns * 100):.2f}%')



