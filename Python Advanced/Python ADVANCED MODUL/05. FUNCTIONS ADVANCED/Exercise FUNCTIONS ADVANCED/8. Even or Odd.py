def even_odd(*args):
    command = args[-1]
    nums_list = args[:-1]
    if command == "even":
        nums = list(filter(lambda x: x % 2 == 0, nums_list))
        return nums

    else:
        nums = list(filter(lambda x: x % 2 == 1, nums_list))
        return nums

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))