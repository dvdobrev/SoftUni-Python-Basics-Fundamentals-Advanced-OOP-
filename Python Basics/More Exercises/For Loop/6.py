months = int(input())
eletricity = 0
water = 20 * months
internet = 15 * months


for i in range(1, months + 1):
    eletricity += float(input())

other = (eletricity + water + internet) * 0.2 + (eletricity + water + internet)
average = (eletricity + water + internet + other) / months
print(f'Electricity: {eletricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')