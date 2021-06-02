l1 = input()
l2 = input()
l3 = input()
counter = 0

for i in range(ord(l1), ord(l2) + 1):
    if i == ord(l3):
        continue
    else:
        for i2 in range(ord(l1), ord(l2) + 1):
            if i2 == ord(l3):
                continue
            else:
                for i3 in range(ord(l1), ord(l2) + 1):
                    if i3 == ord(l3):
                        continue
                    else:
                        counter += 1
                        print(chr(i), end='')
                        print(chr(i2), end='')
                        print(chr(i3), end=' ')



print(counter)