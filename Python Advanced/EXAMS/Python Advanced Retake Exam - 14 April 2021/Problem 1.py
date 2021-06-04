from collections import deque

pizza_orders = deque(int(el) for el in input().split(", "))
employee_pizza_capacity = deque(int(el) for el in input().split(", "))

pizza_count = 0

while True:
    if pizza_orders and employee_pizza_capacity:

        current_pizza_order = pizza_orders[0]
        current_employee_capacity = employee_pizza_capacity[-1]

        if 0 < current_pizza_order <= 10 :
            if current_pizza_order <= current_employee_capacity:
                pizza_count += pizza_orders.popleft()
                employee_pizza_capacity.pop()

            else:
                current_pizza_order -= current_employee_capacity
                employee_pizza_capacity.pop()
                pizza_orders[0] = current_pizza_order
                if employee_pizza_capacity:
                    pizza_count += current_employee_capacity
                    continue
                else:
                    break

        else:
            pizza_orders.popleft()

    else:
        break


if employee_pizza_capacity:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_count}")
    print(f"Employees: ", end="")
    print(*employee_pizza_capacity,  sep=", ")

else:
    print(f"Not all orders are completed.")
    print(f"Orders left: ", end="")
    print(*pizza_orders, sep=", ")