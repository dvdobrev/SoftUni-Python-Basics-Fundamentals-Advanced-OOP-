symbol = input()
c = 0
o = 0
n = 0
word = ''


while symbol != 'End':
    symbol = ord(symbol)

    if c == 1 and o == 1 and n == 1:
        c = 0
        o = 0
        n = 0
        print(word, end=' ')
        word = ''
        if 65 <= symbol <= 90 or 97 <= symbol <= 122:
            word += chr(symbol)
        symbol = input()
        continue

    if symbol == 99 and c == 0:
        c += 1
        if c == 1 and o == 1 and n == 1:
            c = 0
            o = 0
            n = 0
            print(word, end=' ')
            word = ''
        symbol = input()
        continue

    elif symbol == 110 and n == 0:
        n += 1
        if c == 1 and o == 1 and n == 1:
            c = 0
            o = 0
            n = 0
            print(word, end=' ')
            word = ''
        symbol = input()
        continue

    elif symbol == 111 and o == 0:
        o += 1
        if c == 1 and o == 1 and n == 1:
            c = 0
            o = 0
            n = 0
            print(word, end=' ')
            word = ''
        symbol = input()
        continue

    if 65 <= symbol <= 90 or 97 <= symbol <= 122:
        word += chr(symbol)
        if c == 1 and o == 1 and n == 1:
            c = 0
            o = 0
            n = 0
            print(word, end=' ')
            word = ''
        symbol = input()

    else:
        symbol = input()