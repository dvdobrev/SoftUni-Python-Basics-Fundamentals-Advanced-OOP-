command = input()
nums = [int(el) for el in input().split()]

if command == "Odd":
    print(sum(el for el in nums if el % 2 == 1) * len(nums))

else:
    print(sum(el for el in nums if el % 2 == 0) * len(nums))