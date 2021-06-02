n = int(input())

left_sum = 0
right_sum = 0

for i in range(n):
    num = int(input())
    left_sum += num

for g in range(n):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f" Yes, sum = {left_sum}" )
else:
    print(f'No, diff = {abs (left_sum - right_sum)}')