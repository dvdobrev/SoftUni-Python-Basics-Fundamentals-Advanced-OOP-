n1 = int(input())
n2 = int(input())
n3 = int(input())

for i1 in range(1, n1 + 1):
    if i1 % 2 == 0:
        i1 = i1
    else:
        continue
    for i2 in range(2, n2 + 1):
        if i2 == 2 or i2 == 3 or i2 == 5 or i2 == 7:
            i2 = i2
        else:
            continue
        for i3 in range(1, n3 + 1):
            if i3 % 2 == 0:
                i3 = i3
                print(i1, i2, i3)
            else:
                continue

