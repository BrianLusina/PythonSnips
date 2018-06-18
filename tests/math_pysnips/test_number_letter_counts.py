import unittest
from pysnips.math_pysnips.number_letter_counts import number_letter_counts


class NumberLetterCountsTestCase(unittest.TestCase):
    def test_range_1_to_5(self):
        self.assertEqual(19, number_letter_counts(1, 5))

    def test_range_1_to_1000(self):
        self.assertEqual(21124, number_letter_counts(1, 1000))


if __name__ == '__main__':
    unittest.main()
