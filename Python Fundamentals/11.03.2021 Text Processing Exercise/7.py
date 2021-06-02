text = input()
counter = len(text)
explosion_strength = 0
index = 0
new_text = ""
while not counter == 0:
    current_index = text[index]
    if text[index].isdigit():
        explosion_strength += int(text[index])
        for _ in range(explosion_strength):
            if not text[index] == ">" or text[index].isdigit():
                explosion_strength -= 1
                index += 1
            else:
                index += 1
            counter -= 1

    else:
        new_text += text[index]
        index += 1
        counter -= 1
print(new_text)

