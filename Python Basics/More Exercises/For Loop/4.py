students = int(input())

count_students_fail = 0
count_stundets_average = 0
count_stundets_good = 0
count_stundets_very_good = 0
total_grade = 0

for i in range(1, students + 1):
    grade = float(input())
    if 2 <= grade < 3:
        count_students_fail += 1
        total_grade += grade
    elif 3 <= grade < 4:
        count_stundets_average += 1
        total_grade += grade
    elif 4 <= grade < 5:
        count_stundets_good += 1
        total_grade += grade
    elif 5 <= grade:
        count_stundets_very_good += 1
        total_grade += grade
average_grade = total_grade / students

print(f'Top students: {(count_stundets_very_good / students * 100):.2f}%')
print(f'Between 4.00 and 4.99: {(count_stundets_good / students * 100):.2f}%')
print(f'Between 3.00 and 3.99: {(count_stundets_average / students * 100):.2f}%')
print(f'Fail: {(count_students_fail / students * 100):.2f}%')
print(f'Average: {average_grade:.2f}')


