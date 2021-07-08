def fibonacci():
    a, b = 0, 1
    res = []
    while True:
        yield a
        a, b = b, a + b





# def fibonacci():
#     previous_num = 0
#     current_num = 0
#     fibonacci_sum = 0
#     while True:
#         fibonacci_sum = previous_num + current_num
#         if previous_num == 0 and current_num == 0:
#             yield fibonacci_sum
#             previous_num = 1
#             continue
#
#         yield fibonacci_sum
#         previous_num = current_num
#         current_num = fibonacci_sum


generator = fibonacci()
for i in range(5):
    print(next(generator))
