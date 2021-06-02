n = int(input())

for row in range(1, 2):
    print('+', end=' ')
    for r2 in range(n - 2):
        print('-', end=' ')
    print('+', end=' ')
print()
for c1 in range(n - 2):
    for col in range(1, 2):
        print('|', end=' ')
        for r2 in range(n - 2):
            print('-', end=' ')
        print('|', end=' ')
    print()
for row in range(1, 2):
    print('+', end=' ')
    for r2 in range(n - 2):
        print('-', end=' ')
    print('+', end=' ')