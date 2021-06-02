text = input()

emojis = []

for index in range(0, len(text)-1):
    if text[index] == ":":
        emojis.append(f"{text[index]}{text[index+1]}")

print("\n".join(emojis))