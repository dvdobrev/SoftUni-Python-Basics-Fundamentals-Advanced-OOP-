import math

year = input()
p = int(input())  # брой празници в годината
h = int(input())  # брой уикенди, в които Влади си пътува до родния град

weekend = 48
played_sofia = 48 - h
played_varna = h
not_working = played_sofia * 0.75
play_in_holiday = (p / 3) * 2


played = not_working + played_varna + play_in_holiday


if year == 'leap':
    played += played * 0.15
    print(math.floor(played))
else:
    print(math.floor(played))


