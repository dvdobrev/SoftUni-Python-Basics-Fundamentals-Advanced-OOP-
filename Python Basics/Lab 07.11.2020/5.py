destination = input()

while destination != 'End':
    saved_money = 0
    budget = float(input())
    while budget > saved_money:
        money = float(input())
        budget -= money
    print(f'Going to {destination}!')
    destination = input()
