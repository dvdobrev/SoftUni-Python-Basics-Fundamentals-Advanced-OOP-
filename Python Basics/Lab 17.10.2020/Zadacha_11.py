fruit = input()
day = input()
quantity = float(input())

banana = 'banana'
apple = 'apple'
orange = 'orange'
grapefruit = 'grapefruit'
kiwi = 'kiwi'
pineapple = 'pineapple'
grapes = 'grapes'


#working_days == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday'
#weekend = 'Saturday' or 'Sunday'

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        banana = quantity * 2.50
        print(f'{banana:.2f}')
    elif fruit == apple:
        apple = quantity * 1.20
        print(f'{apple:.2f}')
    elif fruit == orange:
        orange = quantity * 0.85
        print(f'{orange:.2f}')
    elif fruit == grapefruit:
        grapefruit = quantity * 1.45
        print(f'{grapefruit:.2f}')
    elif fruit == kiwi:
        kiwi = quantity * 2.70
        print(f'{kiwi:.2f}')
    elif fruit == pineapple:
        pineapple = quantity * 5.50
        print(f'{pineapple:.2f}')
    elif fruit == grapes:
        grapes = quantity * 3.85
        print(f'{grapes:.2f}')
    else:
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        banana = quantity * 2.70
        print(f'{banana:.2f}')
    elif fruit == apple:
        apple = quantity * 1.25
        print(f'{apple:.2f}')
    elif fruit == orange:
        orange = quantity * 0.90
        print(f'{orange:.2f}')
    elif fruit == grapefruit:
        grapefruit = quantity * 1.60
        print(f'{grapefruit:.2f}')
    elif fruit == kiwi:
        kiwi = quantity * 3.00
        print(f'{kiwi:.2f}')
    elif fruit == pineapple:
        pineapple = quantity * 5.60
        print(f'{pineapple:.2f}')
    elif fruit == grapes:
        grapes = quantity * 4.20
        print(f'{grapes:.2f}')
    else:
        print('error')
else:
    print('error')