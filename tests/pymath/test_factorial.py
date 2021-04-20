import unittest

from pymath.factorial import factorial, factorial_digit_sum


class FactorialTests(unittest.TestCase):
    def test_8(self):
        self.assertEqual(40320, factorial(8))

    def test_10(self):
        self.assertEqual(3628800, factorial(10))

    def test_factorial_digit_sum_raises_error(self):
        with self.assertRaises(ValueError):
            factorial_digit_sum("")

        with self.assertRaises(ValueError):
            factorial_digit_sum({})

    def test_digit_sum_of_10(self):
        self.assertEqual(27, factorial_digit_sum(10))

    def test_factorial_5(self):
        self.assertEqual(120, factorial(5))


if __name__ == "__main__":
    unittest.main()
