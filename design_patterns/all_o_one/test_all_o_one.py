import unittest
from typing import List, Tuple
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from design_patterns.all_o_one.all_one import AllOne

ALL_O_ONE_TEST_CASES = [
    (
        [
            ("inc", "apple"),
            ("inc", "banana"),
            ("inc", "apple"),
            ("get_max_key", "apple"),
            ("get_min_key", "banana"),
        ],
    ),
]


class AllOneTestCase(unittest.TestCase):
    @parameterized.expand(ALL_O_ONE_TEST_CASES, name_func=custom_test_name_func)
    def test_all_o_one(self, operations: List[Tuple[str, str]]):
        all_one = AllOne()
        for operation in operations:
            op, value = operation
            match op:
                case "inc":
                    all_one.inc(value)
                case "dec":
                    all_one.dec(value)
                case "get_max_key":
                    actual = all_one.get_max_key()
                    self.assertEqual(value, actual)
                case "get_min_key":
                    actual = all_one.get_min_key()
                    self.assertEqual(value, actual)

    def test_all_o_one_2(self):
        all_one = AllOne()
        all_one.inc("apple")
        all_one.inc("banana")
        all_one.inc("apple")

        actual_apple = all_one.get_max_key()
        expected_apple = "apple"
        self.assertEqual(expected_apple, actual_apple)

        actual_banana = all_one.get_min_key()
        expected_banana = "banana"
        self.assertEqual(expected_banana, actual_banana)


if __name__ == "__main__":
    unittest.main()
