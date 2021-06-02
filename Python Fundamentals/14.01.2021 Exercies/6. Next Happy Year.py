year = int(input())

while True:
    year += 1
    chr_year = str(year)
    if len(chr_year) == len(set(chr_year)):
        print(year)
        break

 1234     12345
4          5