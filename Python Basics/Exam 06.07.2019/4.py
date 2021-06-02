import math

h = int(input())
w = int(input())
percent = int(input()) / 100
walls = (h * w) * 4
volume_to_paint = math.ceil(walls - (walls * percent))

liters = input()
ready = False

while liters != 'Tired!':
    liters = int(liters)
    volume_to_paint -= liters
    if volume_to_paint == 0:
        ready = True
        print(f'All walls are painted! Great job, Pesho!')
        break
    elif volume_to_paint < 0:
        ready = True
        print(f'All walls are painted and you have {abs(volume_to_paint)} l paint left!')
        break
    else:
        liters = input()

if ready == False:
    print(f'{volume_to_paint} quadratic m left.')



