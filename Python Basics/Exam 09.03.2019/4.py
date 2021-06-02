player_name = input()
command = input()
total_points = 301
qurrent_points = 0
good_shot = 0
bad_shot = 0
retire = True

while command != 'Retire':
    sektor = command
    points = int(input())
    if sektor == 'Single':
        total_points -= points
        if total_points < 0:
            total_points = qurrent_points
            bad_shot += 1
        else:
            good_shot += 1
    elif sektor == 'Double':
        total_points -= points * 2
        if total_points < 0:
            total_points = qurrent_points
            bad_shot += 1
        else:
            good_shot += 1
    elif sektor == 'Triple':
        total_points -= points * 3
        if total_points < 0:
            total_points = qurrent_points
            bad_shot += 1
        else:
            good_shot += 1

    if total_points == 0:
        retire = False
        print(f'{player_name} won the leg with {good_shot} shots.')
        break
    qurrent_points = total_points
    command = input()
if retire:
    print(f'{player_name} retired after {bad_shot} unsuccessful shots.')









