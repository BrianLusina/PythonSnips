import unittest

from pyregex.validate_pin import validate_pin


class ValidatePinTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(validate_pin("1234"), True)

    def test_2(self):
        self.assertEqual(validate_pin("12345"), False)

    def test_3(self):
        self.assertEqual(validate_pin("a234"), False)


if __name__ == '__main__':
    unittest.main()
