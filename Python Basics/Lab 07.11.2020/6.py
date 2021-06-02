floors = int(input())
rooms = int(input())

for f in range(floors, 0, - 1):
    room = 0
    office = 0
    for r in range(rooms):
        if f == floors:
            print(f'L{f}{room}', end=' ')
            room += 1
        elif f % 2 == 0:
            print(f'O{f}{office}', end=' ')
            office += 1
        elif f % 2 == 1:
            print(f'A{f}{room}', end=' ')
            room += 1
    print()





