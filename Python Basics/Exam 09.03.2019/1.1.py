year_tax = int(input())

shoes = year_tax * 0.6
suit = shoes * 0.8
ball = suit / 4
others = ball / 5

price = year_tax + shoes + suit + ball + others

print(f'{price:.2f}')