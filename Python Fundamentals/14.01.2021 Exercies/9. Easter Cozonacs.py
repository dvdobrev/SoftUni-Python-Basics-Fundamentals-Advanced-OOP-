budget = float(input())

flour_price = float(input())

eggs_price = 0.75 * flour_price

milk_price = (1.25 * flour_price) / 4

cosonacs = 0
colored_eggs = 0

while budget > 0:
    budget -= flour_price + eggs_price + milk_price
    if budget > 0:
        cosonacs += 1
        colored_eggs += 3
        if cosonacs % 3 == 0:
            colored_eggs -= cosonacs - 2
        continue
    else:
        budget += flour_price + eggs_price + milk_price
        break

print(f"You made {cosonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
