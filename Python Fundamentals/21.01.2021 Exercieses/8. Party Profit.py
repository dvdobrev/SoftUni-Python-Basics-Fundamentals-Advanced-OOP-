party_size = int(input())
days = int(input())

earned_coins = 0
spend_coins = 0
coins_per_companion = 0

for d in range(1, days + 1):
    earned_coins += 50
    if d % 10 == 0:
        party_size -= 2
    if d % 15 == 0:
        party_size += 5
    spend_coins += party_size * 2
    if d % 3 == 0:
        spend_coins += party_size * 3
    if d % 5 == 0:
        earned_coins += party_size * 20
    if d % 5 == 0 and d % 3 == 0:
        spend_coins += party_size * 2
    #coins_per_companion += (earned_coins - spend_coins) // party_size
    #earned_coins = 0
    #spend_coins = 0
coins_per_companion = (earned_coins - spend_coins) // party_size
print(f"{party_size} companions received {coins_per_companion} coins each.")
