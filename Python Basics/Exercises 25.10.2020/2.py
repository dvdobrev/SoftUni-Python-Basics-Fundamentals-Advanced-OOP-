import  sys

n = int(input())

max_number = -sys.maxsize
sum_number = 0

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_number += number

diff = abs(max_number - sum_number)

if max_number == diff:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print('No')
    print(f'Diff = {abs(max_number - diff)}')
