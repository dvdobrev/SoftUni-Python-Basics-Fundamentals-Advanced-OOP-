command = input()
course_name = {}

while not command == "end":
    course, student = command.split(" : ")
    if course not in course_name:
        course_name[course] = []
    course_name[course].append(student)

    command = input()

sorted_course_name = sorted(course_name.items(), key=lambda kvp: len(kvp[1]), reverse=True)

for key, value in sorted_course_name:
    print(f"{key}: {len(value)}")
    v = sorted(value)
    for each in v:
        print(f"-- {each}")