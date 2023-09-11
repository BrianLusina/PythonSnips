import unittest
from . import next_greatest_letter


class NextGreatestLetterTestCase(unittest.TestCase):
    def test_1(self):
        """should return c from ["c", "f", "j"] and target = "a" """
        letters = ["c", "f", "j"]
        target = "a"
        expected = "c"
        actual = next_greatest_letter(letters, target)

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return c from ["c", "f", "j"] and target = "c" """
        letters = ["c", "f", "j"]
        target = "c"
        expected = "f"
        actual = next_greatest_letter(letters, target)

        self.assertEqual(expected, actual)

    def test_3(self):
        """should return c from ["x", "x", "y", "y"] and target = "z" """
        letters = ["x", "x", "y", "y"]
        target = "z"
        expected = "x"
        actual = next_greatest_letter(letters, target)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
