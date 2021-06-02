import sys
import math

snowball_quantity = int(input())

snowball_value = -sys.maxsize
snow = -sys.maxsize
time = -sys.maxsize
quality = -sys.maxsize

for i in range(snowball_quantity):
    snow_for_ball = int(input())
    time_for_ball = int(input())
    quality_for_ball = int(input())
    value = (snow_for_ball / time_for_ball) ** quality_for_ball
    if value > snowball_value:
        snowball_value = value
        snow = snow_for_ball
        time = time_for_ball
        quality = quality_for_ball

print(f"{snow} : {time} = math.trunc{(snowball_value)} ({quality})")

