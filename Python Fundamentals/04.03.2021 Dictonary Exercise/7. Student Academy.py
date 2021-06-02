n_students = int(input())
grades = {}

for student in range(n_students):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_students = {}

for student, value in grades.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        filtered_students[student] = average

sorted_students = sorted(filtered_students.items(), key=lambda kvp: -kvp[1])

for name, grade in sorted_students:
    print(f"{name} -> {grade:.2f}")


