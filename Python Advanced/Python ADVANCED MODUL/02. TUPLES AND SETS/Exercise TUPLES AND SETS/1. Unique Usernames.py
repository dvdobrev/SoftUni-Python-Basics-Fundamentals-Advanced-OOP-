n = int(input())

names = set()

for el in range(n):
    name = input()

    if not name in names:
        names.add(name)
        print(name)