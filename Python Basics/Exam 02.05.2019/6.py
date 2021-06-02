days = int(input())
hours_per_day = int(input())
total_price = 0

for d in range(1, days + 1):
    price_per_day = 0
    for h in range(1, hours_per_day +1):
        if d % 2 == 0 and h % 2 != 0:
            price_per_day += 2.50

        elif d % 2 != 0 and h % 2 == 0:
            price_per_day += 1.25

        else:
            price_per_day += 1

    total_price += price_per_day

    print(f'Day: {d} - {price_per_day:.2f} leva')
print(f'Total: {total_price:.2f} leva')