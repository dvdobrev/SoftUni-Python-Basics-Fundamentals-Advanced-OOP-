numbers = [int(el) for el in input().split()]
numbers_to_remove = int(input())


for n_times in range(numbers_to_remove):
    min_num = min(numbers)
    numbers.remove(min_num)

print(numbers)




