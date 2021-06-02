import math

people = int(input())
capacity = int(input())
courses_needed = math.ceil(people / capacity)
print(courses_needed)
