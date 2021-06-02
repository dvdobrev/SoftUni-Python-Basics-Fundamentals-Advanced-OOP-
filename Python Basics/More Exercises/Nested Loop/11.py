days = int(input())
houers = int(input())
total = 0

for d in range(1, days + 1):
    price = 0
    for h in range(1, houers + 1):
        if d % 2 == 0 and h % 2 != 0:
            price += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f'Day: {d} - {price:.2f} leva')
    total += price
print(f'Total: {total:.2f} leva')