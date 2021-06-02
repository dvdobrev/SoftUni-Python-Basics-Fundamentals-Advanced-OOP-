first_couple = int(input()) #  [10… 90]
second_couple = int(input()) #   [10… 90]
diff_first_couple = int(input()) #разликата между началната и крайната стойност на  първата двойка числа – цяло положително число в диапазона [1… 9]
diff_second_couple = int(input()) # разликата между началната и крайната стойност на  втората двойка числа – цяло положително число в диапазона [1… 9]

for f in range(first_couple, (diff_first_couple + first_couple) + 1):
    counter = 0
    for f1 in range(1, f + 1):
        if f % f1 == 0:
            counter += 1
    if counter == 2:
        for s in range(second_couple, (diff_second_couple + second_couple) + 1):
            counter = 0
            for s1 in range(1, s + 1):
                if s % s1 == 0:
                    counter += 1
            if counter == 2:
                print(f, end='')
                print(s, end='')
                print()





