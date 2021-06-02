import math

income = float(input())
uspeh = float(input())
salary = float(input())

social_scholarship = 0
excellent_scholarship = 0

if uspeh >= 5.5:
   excellent_scholarship += uspeh * 25

if income < salary and uspeh > 4.5:
    social_scholarship += salary * 0.35

if social_scholarship > excellent_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')

    else:
        print('You cannot get a scholarship!')
