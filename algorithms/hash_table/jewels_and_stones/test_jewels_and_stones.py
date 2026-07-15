import unittest
from parameterized import parameterized
from algorithms.hash_table.jewels_and_stones import (
    num_jewels_in_stones_with_dict,
    num_jewels_in_stones_with_set,
)

JEWELS_AND_STONES_TEST_CASES = [
    ("pQ", "ppPQQq", 4),
    ("k", "kkkkK", 4),
    ("LMn", "lLmMNn", 3),
    ("cD", "ddddccccDD", 6),
    ("tRz", "RttZzr", 4),
]


class JewelsAndStonesTestCase(unittest.TestCase):
    @parameterized.expand(JEWELS_AND_STONES_TEST_CASES)
    def test_num_jewels_in_stones_with_set(
        self, jewels: str, stones: str, expected: int
    ):
        actual = num_jewels_in_stones_with_set(jewels, stones)
        self.assertEqual(actual, expected)

    @parameterized.expand(JEWELS_AND_STONES_TEST_CASES)
    def test_num_jewels_in_stones_with_dict(
        self, jewels: str, stones: str, expected: int
    ):
        actual = num_jewels_in_stones_with_dict(jewels, stones)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
