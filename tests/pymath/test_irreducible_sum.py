import unittest

from pymath.irreducible_sum import sum_fracts


class IrreducibleTestCases(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])

    def test_2(self):
        self.assertEqual(sum_fracts([[1, 3], [5, 3]]), 2)


if __name__ == '__main__':
    unittest.main()
