text = input()

stack = []

for el in range(len(text)-1, -1, -1):
    stack.append(text[el])


print("".join(stack))
