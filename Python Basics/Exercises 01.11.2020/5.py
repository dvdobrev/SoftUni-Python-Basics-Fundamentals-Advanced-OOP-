money = float(input())
coins_count = 0
changed_coins = money * 100

while changed_coins >= 1:
    coins_count += 1
    if changed_coins >= 200:
        changed_coins -= 200
    elif changed_coins >= 100:
        changed_coins -= 100
    elif changed_coins >= 50:
        changed_coins -= 50
    elif changed_coins >= 20:
        changed_coins -= 20
    elif changed_coins >= 10:
        changed_coins -= 10
    elif changed_coins >= 5:
        changed_coins -= 5
    elif changed_coins >= 2:
        changed_coins -= 2
    elif changed_coins >= 1:
        changed_coins -= 1
print(coins_count)