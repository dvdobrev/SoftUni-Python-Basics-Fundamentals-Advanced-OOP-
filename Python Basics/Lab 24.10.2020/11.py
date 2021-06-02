age = int(input())
washmaschine = float(input())
toy_price = int(input())

birthday_money = 0
saved_money = 0
saved_toys = 0


for i in range(1, age + 1):
    if i % 2 == 0:
        birthday_money = birthday_money + 10
        saved_money = saved_money + birthday_money
    else:
        saved_toys += + 1

saved_money = saved_money - (age // 2)
saved_toys = saved_toys * toy_price
total_money = saved_toys + saved_money
diff = abs(total_money - washmaschine)

if total_money >= washmaschine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')