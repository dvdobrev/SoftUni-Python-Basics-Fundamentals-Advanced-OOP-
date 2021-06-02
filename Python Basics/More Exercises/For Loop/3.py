total_cargo = int(input())
total_price = 0
average_price = 0
mikrobus = 0
kamion = 0
train = 0

for i in range(1, total_cargo + 1):
    cargo = int(input())
    if cargo <= 3:
        total_price += cargo * 200
        mikrobus += cargo
    elif 3 < cargo <= 11:
        total_price += cargo * 175
        kamion += cargo
    elif cargo > 11:
        total_price += cargo * 120
        train += cargo
total_tons = mikrobus + kamion + train
average_price = total_price / total_tons
percent_mikrobus = mikrobus / total_tons * 100
percent_kamion = kamion / total_tons * 100
percent_train = train / total_tons * 100

print(f'{average_price:.2f}')
print(f'{percent_mikrobus:.2f}%')
print(f'{percent_kamion:.2f}%')
print(f'{percent_train:.2f}%')

