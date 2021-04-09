import unittest

from pystrings.tail_swap import tail_swap


class TailSwapTestCases(unittest.TestCase):
    def test_1(self):
        self.assertEqual(['abc:456', 'cde:123'], tail_swap(['abc:123', 'cde:456']))

    def test_2(self):
        self.assertEqual(['a:xyz', '777:12345'], tail_swap(['a:12345', '777:xyz']))


if __name__ == '__main__':
    unittest.main()
