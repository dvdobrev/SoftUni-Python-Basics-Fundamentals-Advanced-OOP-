name = input()
played_matches = int(input())
total_points = 0
w = 0
d = 0
l = 0

if played_matches == 0:
    print(f'{name} hasn\'t played any games during this season.')
else:
    for match in range(1, played_matches + 1):
        result = input()
        if result == 'W':
            w += 1
            total_points += 3
        elif result == 'D':
            d += 1
            total_points += 1
        elif result == 'L':
            l += 1
    print(f'{name} has won {total_points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {l}')
    print(f'Win rate: {(w / played_matches) * 100:.2f}%')