command = input()
#desi_points = 0
#t2_points = 0
won_match = 0
lost_match = 0

while command != 'End of tournaments':
    match_quantity = int(input())
    for match in range(1, match_quantity + 1):
        desi_points = int(input())
        t2_points = int(input())
        if desi_points > t2_points:
            won_match += 1
            print(f'Game {match} of tournament {command}: win with {desi_points - t2_points} points.')
        else:
            lost_match += 1
            print(f'Game {match} of tournament {command}: lost with {t2_points - desi_points} points.')

    command = input()

total_matches= won_match + lost_match

print(f'{(won_match / total_matches) * 100:.2f}% matches win')
print(f'{(lost_match / total_matches) * 100:.2f}% matches lost')

