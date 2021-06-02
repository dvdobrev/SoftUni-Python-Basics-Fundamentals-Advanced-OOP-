import sys
name = input()
winner_points = -sys.maxsize
winner = ''


while name != 'Stop':
    points = 0
    for l in name:
        number = int(input())
        l = ord(l)
        if number == l:
            points += 10
        else:
            points += 2
    if points >= winner_points:
        winner_points = points
        winner = name

    name = input()

print(f'The winner is {winner} with {winner_points} points!')