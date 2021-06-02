def combinations(text, index):
    if index >= len(text):
        print("".join(text))
        return
    combinations(text, index + 1)
    for i in range(index + 1, len(text)):
        text[index], text[i] = text[i], text[index]
        combinations(text, index + 1)
        text[index], text[i] = text[i], text[index]


text = list(input())
combinations(text, 0)