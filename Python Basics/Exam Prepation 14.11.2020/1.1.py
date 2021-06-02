import math

s = 384400
speed = float(input())
fuel_per_100km = float(input())


houers_to_moon = s / speed
fuel_needed = (s / 100) * fuel_per_100km

print(f'{math.ceil(houers_to_moon * 2) + 3} ')
print(f'{fuel_needed * 2}')