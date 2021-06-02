n = int(input())
salary = int(input())

Facebook = 150
Instagram = 100
Reddit = 50

for i in range(1, n + 1):
    seit_name = input()
    if seit_name == 'Facebook':
        salary += - Facebook
        if salary <= 0:
            print("You have lost your salary.")
    elif seit_name == 'Instagram':
        salary += - Instagram
        if salary <= 0:
            print("You have lost your salary.")
    elif seit_name == 'Reddit':
        salary += - Reddit
        if salary <= 0:
            print("You have lost your salary.")
if salary > 0:
    print(salary)