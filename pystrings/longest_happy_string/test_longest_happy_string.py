import unittest
from parameterized import parameterized
from pystrings.longest_happy_string import longest_diverse_string


class LongestHappyStringTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (2, 2, 2, "abcabc"),
            (0, 5, 5, "bcbcbcbcbc"),
            (6, 3, 0, "aabaabaab"),
            (3, 3, 1, "abababc"),
            (2, 2, 1, "ababc"),
            (5, 1, 0, "aabaa"),
            (7, 2, 0, "aabaabaa"),
            (1, 1, 7, "ccaccbcc"),
        ]
    )
    def test_longest_diverse_string(self, a: int, b: int, c: int, expected):
        actual = longest_diverse_string(a, b, c)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
