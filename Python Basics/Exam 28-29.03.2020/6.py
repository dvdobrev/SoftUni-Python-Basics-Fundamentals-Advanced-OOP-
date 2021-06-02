days = int(input())
money = 0
total_win = 0
total_lose = 0

for i in range(1, days + 1):
    command = input()
    day_win = 0
    day_lose = 0
    while command != 'Finish':
        result = input()
        if result == 'win':
            day_win += 1
        elif result == 'lose':
            day_lose += 1
        command =input()
    day_money = day_win * 20
    if day_win > day_lose:
        day_money += day_money * 0.10
        total_win += 1
    else:
        total_lose += 1
    money += day_money
if total_win > total_lose:
    money = money + (money * 0.20)
    print(f'You won the tournament! Total raised money: {money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money:.2f}')



