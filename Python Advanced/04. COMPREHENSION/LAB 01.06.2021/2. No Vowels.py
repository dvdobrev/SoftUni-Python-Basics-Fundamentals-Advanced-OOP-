text = input()

vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union([el.upper() for el in vowels])

new_text = [el for el in text if not el in vowels]
print("".join(new_text))