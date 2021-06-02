won_battles = 0
energy = int(input())
distance = input()
command_recived = False

while not distance == "End of battle":
    distance = int(distance)
    if energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    else:
        energy -= distance
        won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles

    distance = input()
    if distance == "End of battle":
        command_recived = True

if command_recived:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
