import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def test_init_without_courses(self):
        student = Student("Pesho")
        self.assertEqual("Pesho", student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        courses = {"Math": ["note1"]}
        student = Student("Pesho", courses)
        self.assertEqual("Pesho", student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_existing_course_updates_notes(self):
        student = Student("Pesho", {"Math": ["note1"]})
        result = student.enroll("Math", ["note2", "note3"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "note3"], student.courses["Math"])

    def test_enroll_new_course_with_default_adds_course_and_notes(self):
        student = Student("Pesho")
        result = student.enroll("Math", ["note1"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1"], student.courses["Math"])

    def test_enroll_new_course_with_y_adds_course_and_notes(self):
        student = Student("Pesho")
        result = student.enroll("Math", ["note1"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1"], student.courses["Math"])

    def test_enroll_new_course_with_n_adds_course_without_notes(self):
        student = Student("Pesho")
        result = student.enroll("Math", ["note1"], "N")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], student.courses["Math"])

    def test_add_notes_to_existing_course(self):
        student = Student("Pesho", {"Math": []})
        result = student.add_notes("Math", "note1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1"], student.courses["Math"])

    def test_add_notes_raises_exception_for_missing_course(self):
        student = Student("Pesho")
        with self.assertRaises(Exception) as ex:
            student.add_notes("Math", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_removes_course(self):
        student = Student("Pesho", {"Math": ["note1"]})
        result = student.leave_course("Math")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, student.courses)

    def test_leave_course_raises_exception_for_missing_course(self):
        student = Student("Pesho")
        with self.assertRaises(Exception) as ex:
            student.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()