clothes = [int(a) for a in input().split()]

rack_capacity = int(input())
rack_counter = 1
current_capacity = 0

while clothes:
    current_cloth = clothes.pop()
    current_capacity += current_cloth
    if current_capacity <= rack_capacity:
        continue
    else:
        rack_counter += 1
        current_capacity = current_cloth

print(rack_counter)