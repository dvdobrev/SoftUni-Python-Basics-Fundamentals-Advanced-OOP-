def sum_numbers(n1, n2):
    sum1 = n1 + n2
    return sum1


def subtract(sum1, n3):
    subtract_num = sum1 - n3
    return subtract_num


def add_and_subtract(n1, n2, n3):
    final_num = n1 + n2 - n3
    return final_num


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = add_and_subtract(num1, num2, num3)
print(result)