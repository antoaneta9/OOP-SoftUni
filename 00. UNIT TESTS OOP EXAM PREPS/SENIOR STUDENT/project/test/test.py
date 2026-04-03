from project.senior_student import SeniorStudent
import unittest
import unittest

from project.senior_student import SeniorStudent


class TestSeniorStudent(unittest.TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "John Doe", 4.50)

    def test_init_valid(self):
        self.assertEqual("1234", self.student.student_id)
        self.assertEqual("John Doe", self.student.name)
        self.assertEqual(4.50, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    # student_id tests
    def test_student_id_invalid(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent("123", "John", 4.0)
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_student_id_strips_spaces(self):
        student = SeniorStudent("  5678  ", "John", 4.0)
        self.assertEqual("5678", student.student_id)

    # name tests
    def test_name_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent("1234", "   ", 4.0)
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    # gpa tests
    def test_gpa_invalid(self):
        with self.assertRaises(ValueError) as ex:
            SeniorStudent("1234", "John", 1.0)
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    # apply_to_college tests
    def test_apply_to_college_success(self):
        result = self.student.apply_to_college(4.0, "Harvard")

        self.assertEqual("John Doe successfully applied to Harvard.", result)
        self.assertIn("HARVARD", self.student.colleges)

    def test_apply_to_college_fails(self):
        result = self.student.apply_to_college(5.0, "Harvard")

        self.assertEqual("Application failed!", result)
        self.assertEqual(set(), self.student.colleges)

    def test_apply_to_college_stores_uppercase(self):
        self.student.apply_to_college(4.0, "oxford")
        self.assertIn("OXFORD", self.student.colleges)

    # update_gpa tests
    def test_update_gpa_success(self):
        result = self.student.update_gpa(5.0)

        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(5.0, self.student.student_gpa)

    def test_update_gpa_invalid(self):
        result = self.student.update_gpa(1.0)

        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(4.50, self.student.student_gpa)

    # eq tests
    def test_eq_returns_true(self):
        other = SeniorStudent("5678", "Jane", 4.50)

        self.assertTrue(self.student == other)

    def test_eq_returns_false(self):
        other = SeniorStudent("5678", "Jane", 5.00)

        self.assertFalse(self.student == other)


if __name__ == "__main__":
    unittest.main()