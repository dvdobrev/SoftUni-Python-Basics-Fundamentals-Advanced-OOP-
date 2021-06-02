money = float(input())
year = int(input())

money_left = 0

for i in range (1800, year + 1):
    if i % 2 == 0:
        money -= 12000
    else:
        money -= (12000 + 50 * ((i - 1800) + 18))
if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')