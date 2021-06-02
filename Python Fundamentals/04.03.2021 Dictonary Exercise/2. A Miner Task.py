resource = input()

resource_and_quantity = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in resource_and_quantity:
        resource_and_quantity[resource] = quantity
    else:
        resource_and_quantity[resource] += quantity

    resource = input()

for resource, quantity in resource_and_quantity.items():
    print(f"{resource} -> {quantity}")