import math

hour = int(input())
minutes = int(input())

time = minutes + 15

if time < 60:
    print(f'{hour}:{time}')
elif time > 60:
    hour += 1
    time -= 60
    if hour >= 24:
        hour = 0
    if time < 10:
        print(f'{hour}:0{time}')
    else:
        print(f'{hour}:{time}')
elif time == 60:
    hour += 1
    if hour >= 24:
        hour = 0
    print(f'{hour}:00')
