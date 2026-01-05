import unittest
from typing import List, Tuple
from parameterized import parameterized
from design_patterns.request_logger import RequestLogger

REQUEST_LOGGER_TEST_CASES = [
    (7, [(1, "Good morning", True), (6, "Good morning", False)]),
    (7, [(4, "Hello world", True), (15, "Hello world", True)]),
    (7, [(1, "Hello world", True), (2, "Good morning", True)]),
    (
        7,
        [
            (1, "good morning", True),
            (5, "good morning", False),
            (9, "i need coffee", True),
            (10, "hello world", True),
            (11, "good morning", True),
            (15, "i need coffee", False),
            (17, "hello world", True),
            (25, "i need coffee", True),
        ],
    ),
]


class RequestLoggerTestCases(unittest.TestCase):
    @parameterized.expand(REQUEST_LOGGER_TEST_CASES)
    def test_request_logger(
        self, time_limit: int, requests: List[Tuple[int, str, bool]]
    ):
        request_logger = RequestLogger(time_limit)
        for input_request in requests:
            timestamp, request, expected = input_request
            actual = request_logger.message_request_decision(timestamp, request)
            self.assertEqual(
                expected,
                actual,
                f"Expected {expected}, but got {actual} for timestamp={timestamp}, request={request}",
            )


if __name__ == "__main__":
    unittest.main()
