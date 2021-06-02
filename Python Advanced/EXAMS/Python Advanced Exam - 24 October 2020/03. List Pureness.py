from collections import deque

def best_list_pureness(*test):
    list_to_rotate, rotations_number = deque(test[0]), test[1]
    best_pureness = 0
    rotation_counter = 0

    for i in range(0, rotations_number + 1):
        current_pureness = 0
        for el in list_to_rotate:
            current_pureness += el * list_to_rotate.index(el)
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotation_counter = i
        list_to_rotate.appendleft(list_to_rotate.pop())
    
    return f"Best pureness {best_pureness} after {rotation_counter} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)