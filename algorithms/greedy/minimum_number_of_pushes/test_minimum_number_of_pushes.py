import unittest
from parameterized import parameterized
from algorithms.greedy.minimum_number_of_pushes import (
    minimum_pushes_greedy_with_sorting,
    minimum_pushes_heap,
)

MINIMUM_NUMBER_OF_PUSHES_TO_TYPE_WORD_II_TEST_CASES = [
    ("abcde", 5),
    ("xyzxyzxyzxyz", 12),
    ("aabbccddeeffgghhiiiiii", 24),
    ("wave", 4),
    ("skyskysky", 9),
    ("abbcdeefghhi", 13),
    ("mmmmmmmmmm", 10),
    ("abcdefghijklmnopqrstuvwxyz", 56),
]


class MinimumNumberOfPushesToTypeWordIITestCase(unittest.TestCase):
    @parameterized.expand(MINIMUM_NUMBER_OF_PUSHES_TO_TYPE_WORD_II_TEST_CASES)
    def test_minimum_number_of_pushes_greedy_with_sorting(
        self, word: str, expected: int
    ):
        actual = minimum_pushes_greedy_with_sorting(word)
        self.assertEqual(expected, actual)

    @parameterized.expand(MINIMUM_NUMBER_OF_PUSHES_TO_TYPE_WORD_II_TEST_CASES)
    def test_minimum_number_of_pushes_heap(self, word: str, expected: int):
        actual = minimum_pushes_heap(word)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
