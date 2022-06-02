text = input().split(", ")
result = {el: ord(el) for el in text}
print(result)