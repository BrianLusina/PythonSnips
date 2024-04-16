import unittest

from . import count_students


class StudentsAndLunchTestCases(unittest.TestCase):
    def test_1(self):
        """should return 0 for students = [1,1,0,0], sandwiches = [0,1,0,1]"""
        students = [1, 1, 0, 0]
        sandwiches = [0, 1, 0, 1]
        expected = 0
        actual = count_students(students, sandwiches)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]"""
        students = [1, 1, 1, 0, 0, 1]
        sandwiches = [1, 0, 0, 0, 1, 1]
        expected = 3
        actual = count_students(students, sandwiches)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
