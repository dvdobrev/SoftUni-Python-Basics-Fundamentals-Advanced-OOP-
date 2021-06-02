nums = input()

opposit_nums = []
splited_nums = nums.split()

for i in splited_nums:
    i = int(i)
    opposit_nums.append(-i)

print(opposit_nums)