def stock_availability(inventory_list, command, *products):
    inventory = inventory_list
    command = command
    products = [str(a) for a in products]

    if command == 'delivery':
        for product in products:
            inventory.append(product)


    else:
        if not products:
            inventory.pop(0)

        elif products[0].isdigit():

            index = int(products[0])
            inventory = inventory[index:]

        else:
            for product in products:
                if product in inventory:
                    while product in inventory:
                        inventory.remove(product)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
