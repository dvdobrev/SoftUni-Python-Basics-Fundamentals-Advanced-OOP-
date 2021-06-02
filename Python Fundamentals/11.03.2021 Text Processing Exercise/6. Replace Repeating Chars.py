text = input()

word = []
word.append(text[0])
for index in range(1, len(text)):
    if not text[index]  == text[index-1]:
        word.append(text[index])

print("".join(word))