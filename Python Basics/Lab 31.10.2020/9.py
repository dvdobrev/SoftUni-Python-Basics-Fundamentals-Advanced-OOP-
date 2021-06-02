width = int(input())
long = int(input())
high = int(input())
total_boxes = 0
command = input()
free_space = width * long * high


while command != 'Done':
    boxes = int(command)
    total_boxes += boxes
    if total_boxes < free_space:
        command = input()
    else:
        print(f"No more free space! You need {total_boxes - free_space} Cubic meters more.")
        break
else:
    print(f"{free_space - total_boxes} Cubic meters left.")




