import unittest
from . import min_cost_to_hire_workers


class MinCostToHireWorkersTestCase(unittest.TestCase):
    def test_1(self):
        """quality = [10,20,5], wage = [70,50,30], k = 2 returns 105.00000"""
        quality = [10, 20, 5]
        wage = [70, 50, 30]
        k = 2
        expected = 105.00000
        actual = min_cost_to_hire_workers(quality, wage, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        """quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3 returns 30.66667"""
        quality = [3, 1, 10, 10, 1]
        wage = [4, 8, 2, 2, 7]
        k = 3
        expected = 30.66667
        actual = round(min_cost_to_hire_workers(quality, wage, k), 5)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
