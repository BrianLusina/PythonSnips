import unittest
from . import optimal_task_assignment


class OptimalTaskAssignmentTestCase(unittest.TestCase):
    def test_1(self):
        """Should return [(2,7), (3,6),(5,5)] from [6, 3, 2, 7, 5, 5]"""
        tasks = [6, 3, 2, 7, 5, 5]
        expected = [(2, 7), (3, 6), (5, 5)]
        actual = optimal_task_assignment(tasks)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
