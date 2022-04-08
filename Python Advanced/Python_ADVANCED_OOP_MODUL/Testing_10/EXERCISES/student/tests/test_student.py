from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student1 = Student("Dobri")
        self.student2 = Student("Mariana", {"Python": ["note1"]})

    def test_init(self):
        self.assertEqual("Dobri", self.student1.name)
        self.assertEqual({}, self.student1.courses)

    def test_init_with_courses(self):
        self.assertEqual("Mariana", self.student2.name)
        self.assertEqual({"Python": ["note1"]}, self.student2.courses)

    def test_init_with_no_courses(self):
        self.student2 = Student("Mariana", None)
        self.assertEqual("Mariana", self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_enroll_duplicate_course(self):
        self.student1.courses = {"Python": ["note1"]}
        res = self.student1.enroll("Python", ["note2"])

        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(self.student1.courses["Python"], ["note1", "note2"])


    def test_enroll_new_course_with_notes(self):
        res = self.student1.enroll("Python", ["note1"])
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.student1.courses["Python"], ["note1"])


    def test_enroll_new_course_without_adding_notes(self):
        res = self.student1.enroll("Python", ["note1"], "no")
        self.assertEqual(res, "Course has been added.")
        self.assertEqual(self.student1.courses["Python"], [])


    def test_enroll_new_course_with_adding_notes(self):
        res = self.student1.enroll("Python", ["note1", "note2"], "Y")
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.student1.courses["Python"], ["note1", "note2"])


    def test_enroll_in_existing_course_with_adding_notes(self):
        self.student1.enroll("Python", ["note1", "note2"], "Y")
        res = self.student1.enroll("Python", ["note3"], "Y")

        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(self.student1.courses["Python"], ["note1", "note2", "note3"])


    def test_add_notes(self):
        self.student1.courses = {"Python": []}
        res = self.student1.add_notes("Python", "note1")

        self.assertEqual("Notes have been updated", res)
        self.assertEqual(self.student1.courses["Python"], ["note1"])


    def test_add_notes_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("Java", "note_fail")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual(self.student1.courses, {})


    def test_leave_course(self):
        self.student1.courses = {"Python": []}
        res = self.student1.leave_course("Python")

        self.assertEqual("Course has been removed", res)
        self.assertEqual({}, self.student1.courses)


    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("Java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))







    #
    # def test_attr_are_set(self):
    #     self.assertEqual("Dobri", self.student1.name)
    #     self.assertEqual({}, self.student1.courses)
    #
    # def test_enroll_course_with_notes(self):
    #     result = self.student1.enroll("Python OOP", ["Inheritance", "SOLID"])
    #     self.assertEqual(1, len(self.student1.courses))
    #     self.assertEqual(2, len(self.student1.courses["Python OOP"]))
    #     self.assertEqual("Course and course notes have been added.", result)
    #
    # def test_enroll_course_without_saving_them(self):
    #     result = self.student1.enroll("Python OOP", ["Inheritance", "SOLID"], "N")
    #     self.assertEqual(1, len(self.student1.courses))
    #     self.assertEqual(0, len(self.student1.courses["Python OOP"]))
    #     self.assertEqual("Course has been added.", result)
    #
    # def test_enroll_add_notes_to_exising_course(self):
    #     # Add some course and notes to this student.
    #     result = self.student1.enroll("Python OOP", ["Inheritance", "SOLID"])
    #     self.assertEqual(1, len(self.student1.courses))
    #     self.assertEqual(2, len(self.student1.courses["Python OOP"]))
    #     self.assertEqual("Course and course notes have been added.", result)
    #
    #     # Test if new notes are append to existing course
    #     result = self.student1.enroll("Python OOP", ["Abstraction", "Testing"])
    #     self.assertEqual(1, len(self.student1.courses))
    #     self.assertEqual(4, len(self.student1.courses["Python OOP"]))
    #     self.assertEqual("Course already added. Notes have been updated.", result)
    #
    # def test_add_notes_not_existing_course_raises(self):
    #     with self.assertRaises(Exception) as ex:
    #         self.student1.add_notes("Python OOP", ["1", 2])
    #     self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
    #
    # def test_add_notes_to_existing_course(self):
    #     # Add some course and notes to this student.
    #
    #     result = self.student1.enroll("Python OOP", ["Inheritance", "SOLID"])
    #     self.assertEqual(1, len(self.student1.courses))
    #     self.assertEqual(2, len(self.student1.courses["Python OOP"]))
    #     self.assertEqual("Course and course notes have been added.", result)
    #
    #     # Test notes are append
    #
    #     result = self.student1.add_notes("Python OOP", "Testing")
    #     self.assertEqual("Notes have been updated", result)
    #     self.assertEqual(3, len(self.student1.courses["Python OOP"]))
    #     self.assertIn("Testing", self.student1.courses["Python OOP"])
    #
    # def test_unexsisting_course_removal_raises(self):
    #     with self.assertRaises(Exception) as ex:
    #         self.student1.leave_course("Python OOP")
    #     self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
    #
    # def test_leave_existing_course(self):
    #     result = self.student1.enroll("Python OOP", ["Inheritance", "SOLID"])
    #     self.assertEqual(1, len(self.student1.courses))
    #
    #     # Try to leave the course
    #
    #     result = self.student1.leave_course("Python OOP")
    #     self.assertEqual("Course has been removed", result)
    #     self.assertEqual(0, len(self.student1.courses))


if __name__ == "__main__":
    main()
