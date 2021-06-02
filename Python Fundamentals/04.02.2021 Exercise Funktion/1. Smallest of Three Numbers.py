import sys
def nums(n1, n2, n3):
    smallest_num = sys.maxsize
    if n1 < smallest_num:
        smallest_num = n1
    if n2 < smallest_num:
        smallest_num = n2
    if n3 < smallest_num:
        smallest_num = n3
    return smallest_num


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = nums(num1, num2, num3)
print(result)