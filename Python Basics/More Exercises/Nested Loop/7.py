a = int(input()) + 35
b = int(input()) + 64
max_passwords = int(input())
counter = 0
reached = False

for symbol1 in range(35, a):
    if reached == True:
        break
    if symbol1 > 55:
        symbol1 = 35
    for symbol2 in range(64, b):
        if reached == True:
            break
        if symbol2 > 96:
            symbol2 = 64
        for symbol3 in range(1, (a - 34)):
            for symbol4 in range(1, (b - 63)):
                if symbol3 == (a - 35) and symbol4 == (b - 64):
                    print(chr(symbol1), end='')
                    print(chr(symbol2), end='')
                    print(symbol3, end='')
                    print(symbol4, end='')
                    print(chr(symbol2), end='')
                    print(chr(symbol1), end='')
                    print('|', end='')
                    reached = True
                    break

                if counter == max_passwords:
                    reached = True
                    break
                else:
                    print(chr(symbol1), end='')
                    print(chr(symbol2), end='')
                    print(symbol3, end='')
                    print(symbol4, end='')
                    print(chr(symbol2), end='')
                    print(chr(symbol1), end='')
                    print('|', end='')
                    symbol1 += 1
                    symbol2 += 1
                    counter += 1
