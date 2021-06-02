gradus = int(input())
day_time = input()

if day_time == 'Morning':
    if 10 <= gradus <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < gradus <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
    elif gradus >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")

elif day_time == 'Afternoon':
    if 10 <= gradus <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < gradus <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
    elif gradus >= 25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
        print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
elif day_time == 'Evening' and gradus >= 10:
    Outfit = 'Shirt'
    Shoes = 'Moccasins'
    print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
