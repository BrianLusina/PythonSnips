import unittest
from typing import List, Any
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from datastructures.stacks.freqstack.max_freq_stack import MaxFreqStack

MAX_FREQUENCY_STACK_TEST_CASES = [
    ([5, 7, 7, 7, 4, 5, 3], [7, 5, 7, 3, 4, 7, 5]),
]


class MaxFrequencyStackTestCase(unittest.TestCase):
    @parameterized.expand(
        MAX_FREQUENCY_STACK_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_frequency_stack(self, data: List[Any], expected: List[Any]):
        max_freq_stack = MaxFreqStack()
        for item in data:
            max_freq_stack.push(item)

        for expected_item in expected:
            actual = max_freq_stack.pop()
            self.assertEqual(expected_item, actual)


if __name__ == "__main__":
    unittest.main()
