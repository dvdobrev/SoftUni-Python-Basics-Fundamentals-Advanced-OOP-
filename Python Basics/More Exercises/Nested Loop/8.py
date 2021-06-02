n1 = int(input())
n2 = int(input())
n3 = int(input())

for i1 in range(2, n1 + 1):
    for i2 in range(2, n2 + 1):
        counter = 0
        for i3 in range(2, n3 + 1):
            if i1 % 2 == 0 and i3 % 2 == 0:
                for n in range(1, i2 + 1):
                    conter = counter
                    if i2 % n == 0:
                        counter += 1


                if counter == 2:
                    counter = 0

                    print(i1, end=' ')
                    print(i2, end=' ')
                    print(i3, end=' ')
                    print()

