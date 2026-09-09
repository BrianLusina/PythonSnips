import unittest
from typing import List, Tuple
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from design_patterns.two_sum import TwoSum

TWO_SUM_TEST_CASES = [
    (
        [
            ("add", 5, None),
            ("add", 6, None),
            ("add", 4, None),
            ("find", 11, True),
            ("find", 9, True),
        ],
    ),
    (
        [
            ("add", 1, None),
            ("add", 2, None),
            ("find", 3, True),
            ("add", 4, None),
            ("find", 5, True),
            ("find", 6, True),
        ],
    ),
    (
        [
            ("add", 2, None),
            ("add", 4, None),
            ("add", 6, None),
            ("find", 8, True),
            ("add", 10, None),
            ("find", 12, True),
            ("find", 14, True),
        ],
    ),
    (
        [
            ("add", 3, None),
            ("add", 5, None),
            ("find", 8, True),
            ("find", 10, False),
            ("add", 2, None),
            ("add", 6, None),
            ("find", 11, True),
        ],
    ),
    (
        [
            ("add", 1, None),
            ("find", 1, False),
            ("add", 2, None),
            ("find", 3, True),
            ("add", 2, None),
            ("add", 3, None),
            ("find", 5, True),
        ],
    ),
]


class TwoSumTestCase(unittest.TestCase):
    @parameterized.expand(TWO_SUM_TEST_CASES, name_func=custom_test_name_func)
    def test_two_sum(self, operations: List[Tuple[str, int, bool | None]]):
        two_sum = TwoSum()
        for operation in operations:
            op, num, expected = operation
            match op:
                case "add":
                    two_sum.add(num)
                case "find":
                    actual = two_sum.find(num)
                    self.assertEqual(expected, actual)
                case _:
                    raise ValueError(f"Invalid operation: {op}")


if __name__ == "__main__":
    unittest.main()
