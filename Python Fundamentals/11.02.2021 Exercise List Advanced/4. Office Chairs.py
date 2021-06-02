room_quantity = int(input())
free_chairs = 0
enought_chairs = True

for room in range(1, room_quantity + 1):
    chairs, people = input().split()
    people = int(people)
    difference = abs(len(chairs) - people)
    if len(chairs) < people:
       print(f"{difference} more chairs needed in room {room}")
       enought_chairs = False
    else:
        free_chairs += difference

if enought_chairs:
    print(f"Game On, {free_chairs} free chairs left")


