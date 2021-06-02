n = int(input())
total_sum = 0

for i in range(n):
    char = input()
    number = ord(char)
    total_sum += number

print(f"The sum equals: {total_sum}")


