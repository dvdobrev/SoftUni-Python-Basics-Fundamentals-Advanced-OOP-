text = [el for el in input().split()]
result = [el for el in text if len(el) % 2 == 0]
print(*result, sep="\n")