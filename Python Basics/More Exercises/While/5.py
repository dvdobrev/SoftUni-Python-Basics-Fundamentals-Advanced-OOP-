number = int(input())
total = 0
for i in range(1, number + 1):
    n = int(input())
    total += n
print(f'{total / number:.2f}')
