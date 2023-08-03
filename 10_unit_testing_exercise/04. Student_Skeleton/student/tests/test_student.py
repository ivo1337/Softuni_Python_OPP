from project.student import Student
import unittest

class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Test")

    def test_init(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        student = Student("Test", {"Python": ["note1"]})
        self.assertEqual({"Python": ["note1"]}, student.courses)

    def test_enroll__when_add_course_notes_is_empty_string__expect_to_add_course(self):
        result = self.student.enroll("Python", ["note1", "note2"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)

    def test_enroll__when_add_course_notes_is_Y__expect_to_add_course(self):
        result = self.student.enroll("Python", ["note1", "note2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)

    def test_enroll__when_add_course_notes_is_not_Y__expect_to_add_course(self):
        result = self.student.enroll("Python", ["note1", "note2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python": []}, self.student.courses)


    def test_enroll__when_course_name_is_in_courses__expect_to_add_notes(self):
        self.student.enroll("Python", ["note1", "note2"])
        result = self.student.enroll("Python", ["note3"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)

    def test_add_notes__when_course_name_is_in_courses__expect_to_add_notes(self):
        self.student.enroll("Python", ["note1", "note2"])
        result = self.student.add_notes("Python", "note3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)

    def test_add_notes__when_course_name_is_not_in_courses__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", "note3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course__when_course_name_is_in_courses__expect_to_remove_course(self):
        self.student.enroll("Python", ["note1", "note2"])
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course__when_course_name_is_not_in_courses__expect_to_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    unittest.main()
