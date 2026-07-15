import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.assign_cookies import find_content_children


ASSIGN_COOKIES_TEST_CASES = [
    ([1, 2, 3], [1, 1], 1),
    ([1, 2], [1, 2, 3], 2),
    ([10, 9, 8, 7], [5, 6, 7, 8], 2),
]


class AssignCookiesTestCase(unittest.TestCase):
    @parameterized.expand(ASSIGN_COOKIES_TEST_CASES)
    def test_find_content_children(
        self, greed: List[int], cookies: List[int], expected: int
    ):
        actual = find_content_children(greed, cookies)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
