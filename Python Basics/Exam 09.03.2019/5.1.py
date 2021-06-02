import math

quantity_championships = int(input())
start_points = int(input())
total_points = start_points
wins = 0

for i in range(1, quantity_championships + 1):
    level = input()
    if level == 'W':
        total_points += 2000
        wins += 1
    elif level == 'F':
        total_points += 1200
    elif level == 'SF':
        total_points += 720

average_points = (total_points - start_points) / quantity_championships

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{(wins / quantity_championships) * 100:.2f}%')