def stock_availability(inventory, *args):
    boxes = inventory
    command = args[0]

    if command == "delivery":
        products = list(args[1:])
        for p in products:
            boxes.append(p)

    else:
        element = list(args[1:])
        if not element:
            boxes.pop(0)

        else:
            try:
                if element[0].isalpha:
                    for el in element:
                        while el in boxes:
                            boxes.remove(el)

            except:
                boxes = boxes[element[0]:]

    return boxes


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
#print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
#print(stock_availability(["vanilla", "mocha", "banana"], "sell", 1))