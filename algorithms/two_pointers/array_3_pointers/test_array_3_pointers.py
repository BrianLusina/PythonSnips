import unittest

from . import minimize


class MinimizeTestCase(unittest.TestCase):
    def test_1(self):
        """should return 5 for a= [1, 4, 10], b =[2, 15, 20], c =[10, 12]"""
        a = [1, 4, 10]
        b = [2, 15, 20]
        c = [10, 12]
        expected = 5
        actual = minimize(a, b, c)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 for a= [20, 24, 100], b =[2, 19, 22, 79, 800], c =[10, 12, 23, 24, 119]"""
        a = [20, 24, 100]
        b = [2, 19, 22, 79, 800]
        c = [10, 12, 23, 24, 119]
        expected = 2
        actual = minimize(a, b, c)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
