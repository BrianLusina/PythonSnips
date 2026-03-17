import unittest
from parameterized import parameterized
from algorithms.two_pointers.append_chars_to_make_subsequence import (
    append_characters,
    append_characters_2,
)

APPEND_CHARS_TO_MAKE_SUBSEQUENCE_TEST_CASES = [
    ("a", "a", 0),
    ("a", "b", 1),
    ("z", "zzzz", 3),
    ("cba", "abc", 2),
    ("abcde", "ace", 0),
    ("xyz", "abc", 3),
    ("axbyc", "abcde", 2),
    ("ab", "aba", 1),
    ("abc", "abcbc", 2),
    ("abcde", "a", 0),
    ("coaching", "coding", 4),
    ("z", "abcde", 5),
]


class AppendCharactersTestCase(unittest.TestCase):
    @parameterized.expand(APPEND_CHARS_TO_MAKE_SUBSEQUENCE_TEST_CASES)
    def test_append_characters(self, source: str, target: str, expected: int):
        actual = append_characters(source, target)
        self.assertEqual(expected, actual)

    @parameterized.expand(APPEND_CHARS_TO_MAKE_SUBSEQUENCE_TEST_CASES)
    def test_append_characters_2(self, source: str, target: str, expected: int):
        actual = append_characters_2(source, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
