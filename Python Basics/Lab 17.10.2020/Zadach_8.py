day = input()
ticket = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    print(f'{ticket + 12}')
elif day == 'Wednesday' or day == 'Thursday':
    print(f'{ticket + 14}')
elif day == 'Saturday' or day == 'Sunday':
    print(f'{ticket + 16}')
