number = int(input())

for i in range(1000, 10000):
    i1 = str(i)
    n1 = int(i1[0])
    n2 = int(i1[1])
    n3 = int(i1[2])
    n4 = int(i1[3])
    if n1 != 0 and n2 != 0 and n3 != 0 and n4 != 0:
        if n1 + n2 == n3 + n4:
            if number % (n1 + n2) == 0:
                print(i, end=' ')

            #if (n1 + n2) % number == 0:
                #print(i1, end=' ')