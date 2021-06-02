n = int(input())
l = int(input())
# text = 'abcdefghijklmnopqrstuvwxyz'
y = l + 97
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(97, y):
            for d in range(97, y):
                for e in range(1, n + 1):
                    if a < e > b:
                        print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=' ')