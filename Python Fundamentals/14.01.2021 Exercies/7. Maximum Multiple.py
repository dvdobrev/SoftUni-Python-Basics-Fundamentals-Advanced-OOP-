divisor = int(input())
bound = int(input())

the_number = 0

for i in range(bound, 0, -1):
    if i % divisor == 0:
        the_number = i
        break
print(the_number)
