first_number = int(input())
last_number = int(input())

for i in range(first_number, last_number + 1):
    letter = chr(i)
    print(letter, end=" ")
