n = int(input())
cars = {}

for el in range(n):
    car, mileage, total_fuel = input().split("|")
    cars[car] = []
    cars[car].append(int(mileage))
    cars[car].append(int(total_fuel))

data = input()

while not data == "Stop":
    data = data.split(" : ")
    command = data[0]
    if command == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel_needed = int(data[3])
        for k, v in cars.items():
            if car == k:
                car_mileage = v[0]
                car_fuel = v[1]
                if car_fuel > fuel_needed:
                    cars[k][1] -= fuel_needed
                    cars[k][0] += distance
                    print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
                else:
                    print(f"Not enough fuel to make that ride")
                if cars[k][0] >= 100000:
                    print(f"Time to sell the {car}!")
                    cars.pop(k)
                    break

    elif command == "Refuel":
        car = data[1]
        fuel_to_fill = int(data[2])
        for k, v in cars.items():
            if car == k:
                car_fuel = v[1]
                cars[k][1] += fuel_to_fill
                if cars[k][1] > 75:
                    print(f"{car} refueled with {75 -(cars[k][1] - fuel_to_fill) } liters")
                    cars[k][1] = 75
                else:
                    print(f"{car} refueled with {fuel_to_fill} liters")

    elif command == "Revert":
        car = data[1]
        km_to_revert = int(data[2])
        for k, v in cars.items():
            if car == k:
                car_mileage = v[0]
                car_mileage -= km_to_revert
                if car_mileage < 10000:
                    car_mileage = 10000
                    cars[k][0] = car_mileage
                else:
                    cars[k][0] = car_mileage
                    print(f"{car} mileage decreased by {km_to_revert} kilometers")

    data = input()

cars = dict(sorted(cars.items(), key=lambda kvp: (-kvp[1][0], kvp[0])))

for k,v in cars.items():
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")