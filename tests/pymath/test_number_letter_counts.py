import unittest

from pymath.number_letter_counts import number_letter_counts


class NumberLetterCountsTestCase(unittest.TestCase):
    def test_range_1_to_5(self):
        self.assertEqual(19, number_letter_counts(1, 5))

    def test_range_1_to_1000(self):
        self.assertEqual(21124, number_letter_counts(1, 1000))

    def test_should_raise_value_error_for_none(self):
        with self.assertRaises(ValueError):
            number_letter_counts(None, 10)

        with self.assertRaises(ValueError):
            number_letter_counts(1, None)

    def test_should_raise_value_error_for_non_numbers(self):
        with self.assertRaises(ValueError):
            number_letter_counts("", 19)

        with self.assertRaises(ValueError):
            number_letter_counts(1, "")

        with self.assertRaises(ValueError):
            number_letter_counts(1, {})

    def test_should_return_number_if_given_float(self):
        self.assertEqual(19, number_letter_counts(1, 5.0))


if __name__ == '__main__':
    unittest.main()
