def all_characters(c1, c2):
    c1 = ord(c1) + 1
    c2 = ord(c2)
    searched_characters = []
    for i in range(c1, c2):
       searched_characters.append(chr(i))
    return searched_characters


character1 = input()
character2 = input()

result = all_characters(character1, character2)
print(" ".join(result))
