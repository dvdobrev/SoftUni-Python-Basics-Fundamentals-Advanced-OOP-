#x1 + x2 + x3 = n
n = int(input())
result = 0
for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                result += 1
print(result)