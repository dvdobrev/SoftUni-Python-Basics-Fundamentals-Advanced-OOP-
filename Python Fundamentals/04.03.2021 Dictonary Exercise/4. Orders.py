data = input()
products = {}

while not data == "buy":
    command = data.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

    data = input()

for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")