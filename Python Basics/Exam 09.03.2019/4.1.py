p1 = input()
p2 = input()
command = input()
p1_points = 0
p2_points = 0
winner_points = 0
number_wars = False


while command != 'End of game':
    number1 = int(command)
    number2 = int(input())
    if number1 == number2:
        number1 = int(input())
        number2 = int(input())
        if number1 > number2:
            winner = p1
            winner_points = p1_points
        else:
            winner = p2
            winner_points = p2_points
        number_wars = True
        print('Number wars!')
        print(f'{winner} is winner with {winner_points} points')
        break
    elif number1 > number2:
        p1_points += number1 - number2
    else:
        p2_points += number2 - number1

    command = input()
if number_wars == False:
    print(f'{p1} has {p1_points} points')
    print(f'{p2} has {p2_points} points')

