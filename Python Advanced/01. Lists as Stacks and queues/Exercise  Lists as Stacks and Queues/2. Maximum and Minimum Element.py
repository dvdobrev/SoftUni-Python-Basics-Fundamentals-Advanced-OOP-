n = int(input())
stack = []

for el in range(n):
    data = input().split()
    command = int(data[0])

    if command == 1:
        stack.append(int(data[1]))

    elif command == 2:
        if stack:
            stack.pop()

    elif command == 3:
        if stack:
            print(max(stack))

    elif command == 4:
        if stack:
            print(min(stack))

stack = [str(el) for el in stack]

new_stack = []

while stack:
    new_stack.append(stack.pop())

print(", ".join(new_stack))