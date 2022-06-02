def math_operations(*args, **kwargs):
    args = [el for el in args]
    counter = 0

    for el in args:
        if counter == 4:
            counter = 0
        if counter == 0:
            kwargs["a"] += el
            counter += 1

        elif counter == 1:
            kwargs["s"] -= el
            counter += 1

        elif counter == 2:

            try:
                kwargs["d"] /= el
                counter += 1


            except ZeroDivisionError:
                counter += 1

        elif counter == 3:
            kwargs["m"] *= el
            counter += 1

    args = [el for el in args if not el == 0]

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print()
print(math_operations(6, a=0, s=0, d=0, m=0))
