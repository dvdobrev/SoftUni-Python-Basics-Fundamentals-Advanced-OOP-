from itertools import permutations

def possible_permutations(num_list):
    for perm in permutations(num_list):
        yield list(perm)



[print(n) for n in possible_permutations([1, 2, 3])]