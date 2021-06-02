data = input().split(", ")

valid_username = []

for word in data:
    if 3 < len(word) < 16:
        if "-" not in word and "_" not in word and not word.isalnum():
            continue
        valid_username.append(word)

print("\n".join(valid_username))

