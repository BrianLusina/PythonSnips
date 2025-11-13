import unittest
from . import find_order, can_finish


class FindOrderTestCase(unittest.TestCase):
    def test_1(self):
        num_courses = 2
        prerequisites = [[1,0]]
        expected = [0, 1]
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)

    def test_2(self):
        num_courses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        expected = [0,2,1,3]
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)


    def test_3(self):
        num_courses = 1
        prerequisites = []
        expected = [0]
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)

    def test_4(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1]]
        expected = [0,1,2]
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)

    def test_5(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1],[1,2]]
        expected = []
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)

    def test_6(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1],[4,3]]
        expected = [0,1,2] # or [0,1,2,3,4]
        actual = find_order(num_courses=num_courses, prerequisites=prerequisites)
        self.assertEqual(expected, actual)


class CanFinishTestCases(unittest.TestCase):
    def test_1(self):
        num_courses = 2
        prerequisites = [[1,0]]
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertTrue(actual)

    def test_2(self):
        num_courses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertTrue(actual)

    def test_3(self):
        num_courses = 1
        prerequisites = []
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertTrue(actual)

    def test_4(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1]]
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertTrue(actual)

    def test_5(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1],[1,2]]
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertFalse(actual)

    def test_6(self):
        num_courses = 3
        prerequisites = [[1,0],[2,1],[4,3]]
        actual = can_finish(num_courses=num_courses, prerequisites=prerequisites)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
