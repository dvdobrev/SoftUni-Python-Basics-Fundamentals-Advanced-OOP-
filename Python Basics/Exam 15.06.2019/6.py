a1 = int(input())
a2 = int(input())
n = int(input())

for i in range(a1, a2):
    s1 = i
    s2 = 0
    s3 = 0
    s4 = 0

    if s1 % 2 != 0:
        s1 = chr(s1)
    else:
        continue
    for i2 in range(1, n):
        s2 = i2
        for i3 in range(1, (n // 2)):
            s3 = i3
            s4 = i
            if (s2 + s3 + s4) % 2 != 0:
                print(f'{s1}-{s2}{s3}{s4}')
