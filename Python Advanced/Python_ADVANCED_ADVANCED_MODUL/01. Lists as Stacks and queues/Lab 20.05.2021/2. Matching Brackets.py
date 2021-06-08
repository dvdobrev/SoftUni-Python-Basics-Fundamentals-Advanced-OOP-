text = input()

s = []

for el in range(len(text)):
    ch = text[el]
    if ch == "(":
        s.append(el)
    elif ch == ")":
        j = s.pop()
        print(text[j:el + 1])
