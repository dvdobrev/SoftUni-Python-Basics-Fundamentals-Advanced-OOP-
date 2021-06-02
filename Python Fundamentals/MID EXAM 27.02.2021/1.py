import math

numbers_of_biskuits_per_worker = int(input())
number_of_worker = int(input())
biskuits_of_the_other_factory = int(input())

biskuits_for_20_days = math.floor(numbers_of_biskuits_per_worker * number_of_worker) * 20
biskuits_for_10_days = math.floor((numbers_of_biskuits_per_worker * 0.75) * number_of_worker) * 10
total_biskuits = biskuits_for_10_days + biskuits_for_20_days
difference = (abs(total_biskuits - biskuits_of_the_other_factory) / biskuits_of_the_other_factory) * 100

print(f"You have produced {total_biskuits} biscuits for the past month.")

if total_biskuits > biskuits_of_the_other_factory:
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    print(f"You produce {difference:.2f} percent less biscuits.")



