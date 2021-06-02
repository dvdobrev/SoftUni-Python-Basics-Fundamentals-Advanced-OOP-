jury = int(input()) # peoples_count
presentation_name = input()
all_students_average_assessment = 0 # total_grades
students_count = 0 # total_presentation

while presentation_name != 'Finish':
    average_assesment = 0
    for i in range(1, jury +1):
        grades = float(input())
        average_assesment += grades
    all_students_average_assessment += average_assesment
    print(f'{presentation_name} - {average_assesment / jury:.2f}.')
    students_count += 1
    presentation_name = input()
print(f"Student's final assessment is {(all_students_average_assessment / students_count) / jury:.2f}.")





