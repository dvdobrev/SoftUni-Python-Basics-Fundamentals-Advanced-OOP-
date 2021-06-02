n = int(input())

synonims = {}

for w in range(n):
    word = input()
    synonim = input()
    if not word in synonims:
        synonims[word] = []
    synonims[word].append(synonim)

for key, values in synonims.items():
    print(f"{key} - {', '.join(values)}")
