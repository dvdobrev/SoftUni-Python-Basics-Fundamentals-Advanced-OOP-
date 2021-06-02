control_number = int(input())
counter = 0
found = False
# p - position
p1 = 0
p2 = 0
p3 = 0
p4 = 0

#if 4 < control_number < 144:
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == control_number:
                    if a < b and c > d:
                        counter += 1
                        print(a, end='')
                        print(b, end='')
                        print(c, end='')
                        print(d, end='')
                        print(end=' ')
                        if counter == 4:
                            found = True
                            p1 = a
                            p2 = b
                            p3 = c
                            p4 = d

if found == False:
    print()
    print('No!')
else:
    print()
    print(f'Password: {p1}{p2}{p3}{p4}')