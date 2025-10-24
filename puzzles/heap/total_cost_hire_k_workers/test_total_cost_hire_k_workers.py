import unittest

from . import total_cost


class TotalCostToHireKWorkersTestCase(unittest.TestCase):
    def test_1(self):
        """costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4 should return 11"""
        costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
        k = 3
        candidates = 4
        expected = 11
        actual = total_cost(costs=costs, k=k, candidates=candidates)
        self.assertEqual(expected, actual)

    def test_2(self):
        """costs = [1,2,4,1], k = 3, candidates = 3 should return 4"""
        costs = [1, 2, 4, 1]
        k = 3
        candidates = 3
        expected = 4
        actual = total_cost(costs=costs, k=k, candidates=candidates)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
