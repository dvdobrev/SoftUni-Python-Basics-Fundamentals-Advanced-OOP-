chocolate = [int(el) for el in input().split(", ")]  # last
milk = [int(el) for el in input().split(", ")]  # first

total_milkshakes = 0
is_succesful = False

while True:
    if total_milkshakes >= 5:
        is_succesful = True
        break

    if not chocolate or not milk:
        break

    current_chocolate = chocolate[-1]
    current_milk = milk[0]

    if current_chocolate <= 0:
        chocolate.pop()
        continue

    if current_milk <= 0:
        milk.pop(0)
        continue

    if current_chocolate == current_milk:
        chocolate.pop()
        milk.pop(0)
        total_milkshakes += 1

    else:
        milk.append(current_milk)
        milk.pop(0)
        chocolate[-1] -= 5

if is_succesful:
    print(f"Great! You made all the chocolate milkshakes needed!")
    if chocolate:
        print(f"Chocolate: ", end="")
        print(*chocolate, sep=", ")
    else:
        print(f"Chocolate: empty")

    if milk:
        print(f"Milk: ",end="")
        print(*milk, sep=", ")
    else:
        print(f"Milk: empty")


else:
    print(f"Not enough milkshakes.")
    if chocolate:
        print(f"Chocolate: ", end="")
        print(*chocolate, sep=", ")
    else:
        print(f"Chocolate: empty")

    if milk:
        print(f"Milk: ",end="")
        print(*milk, sep=", ")
    else:
        print(f"Milk: empty")

