number1 = int(input())
number2 = int(input())


for number in range(number1, number2 + 1):
    count = 1
    even = 0
    odd = 0
    for digit in str(number):
        if count % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
        count += 1

    if even == odd:
        print(number, end=' ')

        # 123456
        # 123460