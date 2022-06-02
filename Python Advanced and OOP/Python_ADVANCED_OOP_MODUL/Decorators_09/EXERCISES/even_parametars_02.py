def even_parameters(func):
    def wrapper(*args):
        try:
            not_even_nums = [num for num in args if not num % 2 == 0]
            if not_even_nums:
                return f"Please use only even numbers!"

            else:
                return func(*args)

        except TypeError:
            return f"Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# 6
# Please use only even numbers!


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

# 384
# Please use only even numbers!
