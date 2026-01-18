import unittest
from parameterized import parameterized
from algorithms.dynamic_programming.decodeways import num_decodings

NUM_DECODINGS_TEST_CASES = [
    ("11106", 2),
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("101", 1),
    ("12", 2),
    ("012", 0),
    ("0", 0),
    ("30", 0),
    ("10", 1),
    ("27", 1),
]


class NumDecodingsTestCase(unittest.TestCase):
    @parameterized.expand(NUM_DECODINGS_TEST_CASES)
    def test_num_decodings(self, s: str, expected: int):
        actual = num_decodings(s)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
