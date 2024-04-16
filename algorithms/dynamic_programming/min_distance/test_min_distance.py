import unittest
from . import min_distance, min_distance_memoization


class MinDistanceTestCase(unittest.TestCase):
    def test_same_words_return_0(self):
        """should return 0 from a = abcd and b=abcd"""
        a = "abcd"
        b = "abcd"
        expected = 0
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)

    def test_empty_word_a_returns_length_of_b(self):
        """should return 4 from a = '' and b=abcd"""
        a = ""
        b = "abcd"
        expected = 4
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)

    def test_abad_and_abac(self):
        """should return 1 from a = abad and b=abac"""
        a = "abad"
        b = "abac"
        expected = 1
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)

    def test_Anshuman_and_Antihuman(self):
        """should return 2 from a = Anshuman and b=Antihuman"""
        a = "Anshuman"
        b = "Antihuman"
        expected = 2
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)

    def test_horse_and_rose(self):
        """should return 3 from a = horse and b=ros"""
        a = "horse"
        b = "ros"
        expected = 3
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)

    def test_intention_and_execution(self):
        """should return 3 from a = intention and b=execution"""
        a = "intention"
        b = "execution"
        expected = 5
        actual = min_distance(a, b)
        self.assertEqual(expected, actual)


class MinDistanceMemoTestCase(unittest.TestCase):
    def test_same_words_return_0(self):
        """should return 0 from a = abcd and b=abcd"""
        a = "abcd"
        b = "abcd"
        expected = 0
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)

    def test_empty_word_a_returns_length_of_b(self):
        """should return 4 from a = '' and b=abcd"""
        a = ""
        b = "abcd"
        expected = 4
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)

    def test_abad_and_abac(self):
        """should return 1 from a = abad and b=abac"""
        a = "abad"
        b = "abac"
        expected = 1
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)

    def test_Anshuman_and_Antihuman(self):
        """should return 2 from a = Anshuman and b=Antihuman"""
        a = "Anshuman"
        b = "Antihuman"
        expected = 2
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)

    def test_horse_and_rose(self):
        """should return 3 from a = horse and b=ros"""
        a = "horse"
        b = "ros"
        expected = 3
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)

    def test_intention_and_execution(self):
        """should return 3 from a = intention and b=execution"""
        a = "intention"
        b = "execution"
        expected = 5
        actual = min_distance_memoization(a, b)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
