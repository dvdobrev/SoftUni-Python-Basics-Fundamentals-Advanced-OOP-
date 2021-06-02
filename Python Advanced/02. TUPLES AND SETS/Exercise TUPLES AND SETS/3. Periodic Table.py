n = int(input())

elements = set()

for i in range(n):
    data = input().split()
    for el in data:
        if not el in elements:
            elements.add(el)

for el in elements:
    print(el)