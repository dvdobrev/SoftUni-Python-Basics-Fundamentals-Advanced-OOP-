command = input()
goal = 10000

while command != 'Going home':
    steps = int(command)
    goal -= steps
    if goal > 0:
        command = input()
    else:
        print(f'Goal reached! Good job!\n{abs(goal)} steps over the goal!')
        break
else:
    steps = int(input())
    goal -= steps
    if goal > 0:
        print(f'{goal} more steps to reach goal.')
    else:
        print(f'Goal reached! Good job!\n{abs(goal)} steps over the goal!')


