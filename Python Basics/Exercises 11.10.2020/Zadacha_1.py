import math


time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

mins = total_time / 60
seconds = total_time % 60

mins = math.floor(mins)

if seconds < 10:
    print(f'{mins}:0{seconds}')
else:
    print(f'{mins}:{seconds}')

