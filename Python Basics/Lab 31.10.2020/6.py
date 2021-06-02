import sys

command = input()
biggest_number = sys.maxsize

while command != 'Stop':
    number = int(command)
    if number < biggest_number:
        biggest_number = number
    command = input()
print(biggest_number)