water_tank = 255  #liters

line_numbers = int(input())

for i in range(line_numbers):
    quantity_water = int(input())
    water_tank -= quantity_water
    if water_tank >= 0:
        continue
    else:
        water_tank += quantity_water
        print("Insufficient capacity!")
        continue
print(255 - water_tank)



