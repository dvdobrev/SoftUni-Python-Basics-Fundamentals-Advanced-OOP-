def numbers_searching(*args):
    numbers = args
    min_number = min(args)
    max_number = max(args)
    duplicates = []
    missing_number = -999999999

    for el in numbers:
        if numbers.count(el) > 1 and el not in duplicates:
            duplicates.append(el)
    duplicates = sorted(duplicates)
    for el in range(min_number, max_number):
        if el not in numbers:
            missing_number = el

    return [missing_number, sorted(duplicates)]

#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
