from project.employee import Employee
from Python_ADVANCED_OOP_MODUL.Inheritance_05.EXERCISES.project_person_01.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return f"teaching..."

teacher = Teacher()
#
# print(teacher.teach())
# print(teacher.sleep())
# print(teacher.get_fired())
#
#
