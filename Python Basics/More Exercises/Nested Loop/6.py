last_sektor = input()
row_on_first_sektor = int(input())
sits_on_odd_row = int(input()) + 97
sits_on_even_row = sits_on_odd_row + 2
last_sektor = ord(last_sektor)
# 97 - 122

total_sits = 0

for sektor in range(65, last_sektor + 1):
    for row in range(1, row_on_first_sektor + 1):
        if row % 2 != 0:
            for sits in range(97, sits_on_odd_row):
                total_sits += 1
                print(f'{chr(sektor)}{row}{chr(sits)}')
        else:
            for sits in range(97, sits_on_even_row):
                total_sits += 1
                print(f'{chr(sektor)}{row}{chr(sits)}')

    row_on_first_sektor += 1
print(total_sits)
