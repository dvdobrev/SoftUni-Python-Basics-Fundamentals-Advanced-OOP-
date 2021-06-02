n = int(input())

for row in range(1, n + 1):
    if row < n:
        print(' ', end='')
    else:
        print('*')
        for r in range(row - 1):
            print(' *', end='')
print()

for x in range(1, n + 1):
    if x < n:
        print(' *', end='')
    else:
        print()
        for r in range(x - 1):
            print(' ', end='')
print('*')
