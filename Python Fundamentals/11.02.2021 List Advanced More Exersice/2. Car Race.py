numbers = [int(el) for el in input().split()]
middle = int((len(numbers) + 1) / 2)
left_racer = numbers[0: middle - 1]
right_racer = numbers[middle:]
reversed_right_racer = list(reversed(right_racer))
sum_left_racer = 0
sum_right_racer = 0

for left in (left_racer):
    if left == 0:
        sum_left_racer *= 0.8
    else:
        sum_left_racer += left

for right in (reversed_right_racer):
    if right == 0:
        sum_right_racer *= 0.8
    else:
        sum_right_racer += right

# if sum_left_racer < sum_right_racer:
#     print(f"The winner is left with total time: {sum_left_racer:.1f}")
# elif sum_right_racer < sum_left_racer:
#     print(f"The winner is right with total time: {sum_right_racer}")

print(left_racer)
print(right_racer)