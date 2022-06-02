#nums = [int(el) for el in input().split()]
#filterd_nums = print([el for el in nums if el % 2 == 0])


nums = map(int, input().split())
print(list(filter(lambda x: x % 2 == 0, nums)))