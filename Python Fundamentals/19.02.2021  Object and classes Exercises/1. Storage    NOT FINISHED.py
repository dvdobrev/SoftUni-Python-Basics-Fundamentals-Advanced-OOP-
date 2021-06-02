data = input()

products = {}

while not data == "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)
    products[product] += quantity

    data = input()
    # if product not in products:
    #     products[product] = quantity
    # else:
    #     products[product] += quantit

print(products)