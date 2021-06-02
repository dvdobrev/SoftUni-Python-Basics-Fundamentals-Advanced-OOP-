budget = float(input())
season = input() # "summer” или "winter”

resting = ''
destination = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        resting = 'Camp'
        price = budget * 0.3
    elif season == 'winter':
        resting = 'Hotel'
        price = budget * 0.7


elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        resting = 'Camp'
        price = budget * 0.4
    elif season == 'winter':
        resting = 'Hotel'
        price = budget * 0.8

elif budget > 1000:
    destination = 'Europe'
    resting = 'Hotel'
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{resting} - {price:.2f}")