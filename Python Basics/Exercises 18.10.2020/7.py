month = input()   # May, June, July, August, September или October;
nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 14 >= nights > 7:
        studio_price -= studio_price * 0.05
    elif nights > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price -= apartment_price * 0.10

total_price_studio = studio_price * nights
total_price_apartment = apartment_price * nights

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
