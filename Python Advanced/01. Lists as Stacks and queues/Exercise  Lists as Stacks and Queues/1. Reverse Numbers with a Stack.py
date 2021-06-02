num = [el for el in input().split()]

reversed_num = []

while num:
    reversed_num.append(num.pop())

print(" ".join(reversed_num))