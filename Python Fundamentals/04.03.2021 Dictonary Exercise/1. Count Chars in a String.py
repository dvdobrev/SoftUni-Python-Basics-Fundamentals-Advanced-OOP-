text = input()

text_dictonary = {}

for el in text:
    if not el == " ":
        if el not in text_dictonary:
            text_dictonary[el] = 1
        else:
            text_dictonary[el] += 1

for chr, value in text_dictonary.items():
    print(f"{chr} -> {value}")
