import unittest
from typing import List, Tuple
from parameterized import parameterized
from design_patterns.continuous_median import ContinuousMedianHandler

CONTINUOUS_MEDIA_HANDLER_TESTS = [
    (
        ([(1, 2), 1.50000], [(3), 2.00000]),
    ),
]


class ContinuousMedianHandlerTestCase(unittest.TestCase):
    @parameterized.expand(CONTINUOUS_MEDIA_HANDLER_TESTS)
    def test_continuous_median_handler(self, requests: List[Tuple[List[Tuple[int]] | int, int | float]]):
        median_handler = ContinuousMedianHandler()
        for request in requests:
            data, expected = request
            if type(data) is int:
                median_handler.insert(data)
            else:
                for d in data:
                    median_handler.insert(d)

            actual = median_handler.get_median()
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
