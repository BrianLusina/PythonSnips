import unittest
from parameterized import parameterized
from algorithms.hash_table.first_unique_character import first_unique_character

FIRST_UNIQUE_CHARACTER_TEST_CASES = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("baefeab", 3),
    ("aabbcc", -1),
    ("dajhfiuebdafsdhdgaj", 5),
    ("xyurtwxwtryua", 12),
    ("aeiouqwertyauieotweryqq", -1),
    ("awsjuhfajwfnkag", 2),
]


class FirstUniqueCharacterTestCase(unittest.TestCase):
    @parameterized.expand(FIRST_UNIQUE_CHARACTER_TEST_CASES)
    def test_first_unique_character(self, s: str, expected: int):
        actual = first_unique_character(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
