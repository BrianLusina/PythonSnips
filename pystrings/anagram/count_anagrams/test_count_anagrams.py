import unittest
from parameterized import parameterized
from pystrings.anagram.count_anagrams import count_anagrams

COUNT_ANAGRAMS_TEST_CASES = [
    ("too hot", 18),
    ("aa", 1),
    ("all good", 36),
    ("a a a b b", 1),
    ("hello world", 7200),
    ("excel", 60),
    ("ab ab cd cd ef ef", 64),
]


class CountAnagramsTestCase(unittest.TestCase):
    @parameterized.expand(COUNT_ANAGRAMS_TEST_CASES)
    def test_count_anagrams(self, s: str, expected: int):
        actual = count_anagrams(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
