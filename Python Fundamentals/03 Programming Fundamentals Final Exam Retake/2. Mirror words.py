import re

text = input()

pattern = r"(@|#)[A-Za-z]{2}[A-Za-z]+\1\1[A-Za-z]{2}[A-Za-z]+\1"

valid_words = [el.group() for el in re.finditer(pattern, text)]
valid_words_as_string = "".join(valid_words)
word_pattern = r"(?<=(@|#))[A-Za-z]{2}[A-Za-z]+"
words = [el.group() for el in re.finditer(word_pattern, valid_words_as_string)]
mirror_words = []

for word in range(0, len(words), 2):
    first_word = words[word]
    second_word = words[word + 1]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word)
        mirror_words.append(second_word)

if not valid_words == []:
    print(f"{len(valid_words)} word pairs found!")
else:
    print(f"No word pairs found!")


if not mirror_words == []:
    print(f"The mirror words are:")
    for word in range(0, len(mirror_words), 2):
        first_word = mirror_words[word]
        second_word = mirror_words[word + 1]
        if not word == len(mirror_words) - 2:
            print(f"{first_word} <=> {second_word}", end=", ")
        else:
            print(f"{first_word} <=> {second_word}")
else:
    print(f"No mirror words!")