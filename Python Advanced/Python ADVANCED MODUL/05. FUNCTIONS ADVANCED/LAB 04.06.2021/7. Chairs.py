from itertools import combinations

"""" Това е ако се ползва без колекцията по-горе. Но в тази колекцията това всичко е вградено и няма нужда да се пише """
def calc_combinations(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combinations(names[i+1:], n, combs)
        combs.pop()

# Peter, George, Amy

names = input().split(", ")
n = int(input())

calc_combinations(names, n)


# """ Вариант 2 """
# names = input().split(", ")
# n = int(input())
#
# print(*[f"{', '.join(el)}" for el in list(combinations(names, n))], sep='\n')