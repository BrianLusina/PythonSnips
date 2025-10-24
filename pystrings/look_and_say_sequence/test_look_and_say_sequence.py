import unittest
from . import look_and_say_sequence


class LookAndSaySequenceTestCases(unittest.TestCase):
    def test_1(self):
        """sequence of 1 should return 11"""
        sequence = "1"
        expected = "11"
        actual = look_and_say_sequence(sequence)
        self.assertEqual(expected, actual)

    def test_2(self):
        """sequence of 11 should return 21"""
        sequence = "11"
        expected = "21"
        actual = look_and_say_sequence(sequence)
        self.assertEqual(expected, actual)

    def test_3(self):
        """sequence of 21 should return 1211"""
        sequence = "21"
        expected = "1211"
        actual = look_and_say_sequence(sequence)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
