import unittest

from . import generate_permutations


class GenerateAllPermutationsTestCase(unittest.TestCase):
    def test_ab(self):
        """ab should return [ab, ba]"""
        input_ = "ab"
        expected = ["ab", "ba"]
        actual = generate_permutations(input_)
        self.assertEqual(expected, actual)

    def test_abc(self):
        """abc should return [abc,acb,bac,bca,cab,cba]"""
        input_ = "abc"
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        actual = generate_permutations(input_)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
