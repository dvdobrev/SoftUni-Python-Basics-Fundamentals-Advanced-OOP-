money_needed = float(input())
money = float(input())
text = ''
days_spend = 5
days_count = 0


while money_needed > money:
    text = input()
    days_count += 1
    if text == 'spend':
        money_spend = float(input())
        money -= money_spend
        if money_spend > money:
            money = 0
        days_spend -= 1
        if days_spend == 0:
            print(f"You can't save the money.\n{days_count}")
            break
    if text == 'save':
        money += float(input())
        days_spend = 5
else:
    print(f'You saved the money for {days_count} days.')





