import unittest
from parameterized import parameterized
from algorithms.hash_table.ransom_note import can_construct, can_construct_2

RANSOM_NOTE_TEST_CASES = [
    (
        "long_note_success",
        "codinginterviewquestions",
        "aboincsdefoetingvqtniewonoregessnutins",
        True,
    ),
    ("missing_letter", "code", "coingd", False),
    ("shuffled_letters", "codinginterview", "vieewidingcodinter", True),
    ("subset_of_magazine", "program", "programming", True),
    ("repeated_letters", "me", "meme", True),
    ("single_char_mismatch", "a", "b", False),
    ("insufficient_repeated_char", "aa", "ab", False),
    ("sufficient_repeated_char", "aa", "aab", True),
    ("empty_ransom_note", "", "abc", True),
    ("empty_magazine", "a", "", False),
]


class RansomNoteTestCase(unittest.TestCase):
    @parameterized.expand(RANSOM_NOTE_TEST_CASES)
    def test_can_construct(self, _, ransom_note: str, magazine: str, expected: bool):
        actual = can_construct(ransom_note, magazine)
        self.assertEqual(expected, actual)

    @parameterized.expand(RANSOM_NOTE_TEST_CASES)
    def test_can_construct_2(self, _, ransom_note: str, magazine: str, expected: bool):
        actual = can_construct_2(ransom_note, magazine)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
