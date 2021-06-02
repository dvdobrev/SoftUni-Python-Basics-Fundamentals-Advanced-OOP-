def is_number_perfect(n):
    devisior_sum = 0
    perfect_number = True
    for num in range(1, n):
        if n % num == 0:
            devisior_sum += num

    if not devisior_sum == n:
        perfect_number = False
    return perfect_number


number = int(input())

result = is_number_perfect(number)
if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")