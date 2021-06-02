from collections import deque

food = int(input())

list_orders = [int(el) for el in input().split()]

orders = deque(list_orders)
print(max(orders))

while orders:
    current_food = orders.popleft()
    if food >= current_food:
        food -= current_food
    else:
        orders.appendleft(current_food)
        print("Orders left: ", end="")
        for el in orders:
            print(el, end=" ")
        break

if not orders:
    print("Orders complete")