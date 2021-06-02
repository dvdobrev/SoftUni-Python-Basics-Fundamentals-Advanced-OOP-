def even_odd(n):
    even_sum = 0
    odd_sum = 0
    n = str(n)
    for digit in n:
        digit = int(digit)
        if digit == 0:
            continue
        elif digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    #print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
    return [odd_sum, even_sum]

number = int(input())

result = even_odd(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")