import math

price_racket = float(input())
quantity_rackets = int(input())
quantity_shoes = int(input())
shoes = price_racket / 6
total_price_racket = price_racket * quantity_rackets
total_price_shoes = quantity_shoes * shoes
others = (total_price_racket + total_price_shoes) * 0.2

total_price = total_price_shoes + total_price_racket + others
Djokovic_price = total_price / 8
sponsor_price = total_price - Djokovic_price

print(f'Price to be paid by Djokovic {math.floor(Djokovic_price)}')
print(f'Price to be paid by sponsors {math.ceil(sponsor_price)}')
