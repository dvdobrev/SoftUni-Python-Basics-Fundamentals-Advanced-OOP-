import re

n = int(input())

pattern = r"@#+[A-Z][a-zA-Z0-9]{3}[a-zA-Z0-9]+[A-Z]@#+"

for code in range(n):
    barcod = input()
    number = ""
    if re.search(pattern, barcod):
        for el in barcod:
            if el.isnumeric():
                number += el
        if number == "":
            print(f"Product group: 00")
        else:
            print(f"Product group: {number}")

    else:
        print(f"Invalid barcode")