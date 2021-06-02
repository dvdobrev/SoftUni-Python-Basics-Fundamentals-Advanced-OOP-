text = input().split("|")
text = [el.split() for el in text[::-1]]

text = [[int(col) for col in row] for row in text]

#text = text[::-1] обърнал съм го директно във 2рия ред

for row in text:
    for col in row:
        print(col, end=" ")
