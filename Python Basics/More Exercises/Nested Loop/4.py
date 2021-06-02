n1 = int(input())
n4 = int(input())

for i1 in range(n1, n4 + 1):
    for i2 in range(n1, n4 + 1):
        for i3 in range(n1, n4 + 1):
            for i4 in range(n1, n4 + 1):
                if i1 % 2 == 0 and i4 % 2 != 0:
                    if i1 > i4 and (i2 + i3) % 2 == 0:
                        print(i1, end='')
                        print(i2, end='')
                        print(i3, end='')
                        print(i4, end=' ')

                elif i1 % 2 != 0 and i4 % 2 == 0:
                    if i1 > i4 and (i2 + i3) % 2 == 0:
                        print(i1, end='')
                        print(i2, end='')
                        print(i3, end='')
                        print(i4, end=' ')