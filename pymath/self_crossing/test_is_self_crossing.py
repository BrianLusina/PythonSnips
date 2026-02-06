import unittest
from typing import List
from parameterized import parameterized
from pymath.self_crossing import is_self_crossing

IS_SELF_CROSSING_TEST_CASES = [
    ([2, 1, 1, 2], True),
    ([1, 1, 2, 1, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 2, 2, 1, 1], True),
    ([1, 1, 1, 2, 1], True),
    ([1, 1, 2, 2, 3, 3, 4, 4, 10, 4, 4, 3, 3, 2, 2, 1, 1], False),
]


class IsSelfCrossingTestCase(unittest.TestCase):
    @parameterized.expand(IS_SELF_CROSSING_TEST_CASES)
    def test_is_self_crossing(self, distance: List[int], expected: bool):
        actual = is_self_crossing(distance)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
