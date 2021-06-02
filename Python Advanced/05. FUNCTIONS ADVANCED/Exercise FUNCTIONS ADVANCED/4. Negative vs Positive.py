# nums = [int(el) for el in input().split()]
#
# positive_nums = sum([el for el in nums if el >= 0])
# negative_nums = sum([el for el in nums if el < 0])
#
# print(negative_nums)
# print(positive_nums)
#
# if abs(negative_nums) > positive_nums:
#     print(f"The negatives are stronger than the positives")
#
# else:
#     print(f"The positives are stronger than the negatives")

def sum_nums(*args):
    positive_nums = sum(list(filter(lambda x: x >= 0, nums)))
    negative_nums = sum(list(filter(lambda x: x < 0, nums)))
    print(negative_nums)
    print(positive_nums)
    if abs(negative_nums) > positive_nums:
        return print("The negatives are stronger than the positives")
    else:
        return print("The positives are stronger than the negatives")
    

nums = [int(el) for el in input().split()]
sum_nums(nums)