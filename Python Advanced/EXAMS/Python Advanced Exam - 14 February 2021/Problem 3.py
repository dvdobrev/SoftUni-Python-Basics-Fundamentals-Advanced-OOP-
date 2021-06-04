def stock_availability(*args):
    text = args
    cupcakes = args[0]
    command = args[1]

    if command == "delivery":
        products = text[2:]
        for el in products:
            cupcakes.append(el)

    else:
        try:  # if there is an index 2
            produkts = text[2:]
            produkt = str(text[2])
            if produkt.isdigit():
                sold_produkts = int(produkt)
                if sold_produkts <= len(cupcakes):
                    for i in range(sold_produkts):
                        cupcakes = cupcakes[sold_produkts + 1:]

            else:
                for el in produkts:
                    if el in cupcakes:
                        while el in cupcakes:
                            cupcakes.remove(el)

        except IndexError:
            cupcakes.pop(0)


    return cupcakes

# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "banana" , "vanilla", "banana"))
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
