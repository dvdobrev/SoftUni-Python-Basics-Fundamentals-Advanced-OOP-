n = int(input())
name = ""
age = 0

for each in range(n):
    text = input().split()
    for word in range(len(text)):
        if "@" in text[word] and "|" in text[word]:
            text[word] = text[word].replace("@", "")
            text[word] = text[word].replace("|", "")
            name += text[word]
        if "#" in text[word] and "*" in text[word]:
            text[word] = text[word].replace("#", "")
            text[word] = text[word].replace("*", "")
            age = text[word]
    print(f"{name} is {age} years old.")
    name = ""
    age = 0
