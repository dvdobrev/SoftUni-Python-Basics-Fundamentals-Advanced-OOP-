rekord = float(input())  # in seconds
distance = float(input())  # in meters
time_per_meter = float(input())  # seconds

slowly = (distance // 50) * 30
Georgis_time = distance * time_per_meter + slowly
diff = abs(rekord - Georgis_time)


if Georgis_time < rekord:
    print(f'Yes! The new record is {Georgis_time:.2f} seconds.')
else:
    print(f"No! He was {diff:.2f} seconds slower.")