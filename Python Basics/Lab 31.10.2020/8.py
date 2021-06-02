name = input()
total_grade = 0
average_grade = 0
counter = 0
fails = 0

while counter < 12:
    grade = float(input())
    if grade >= 4.00:
        counter += 1
        fails = 0
        total_grade += grade
    else:
        fails += 1
    if fails == 2:
        print(f"{name} has been excluded at {counter + 1} grade")
        break
if counter == 12:
    average_grade = total_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")