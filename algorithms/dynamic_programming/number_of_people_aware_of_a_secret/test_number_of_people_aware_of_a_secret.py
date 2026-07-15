import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.dynamic_programming.number_of_people_aware_of_a_secret import (
    people_aware_of_secret,
    people_aware_of_secret_simulation_deque,
)

PEOPLE_AWARE_OF_A_SECRET_TEST_CASES = [
    (6, 2, 4, 5),
    (4, 1, 3, 6),
    (2, 1, 2, 2),
    (10, 3, 7, 15),
    (10, 3, 5, 5),
    (10, 9, 10, 2),
    (12, 3, 4, 1),
    (1000, 1, 1000, 344211605),
    (100, 10, 50, 22517820),
]


class PeopleAwareOfASecretTestCase(unittest.TestCase):
    @parameterized.expand(
        PEOPLE_AWARE_OF_A_SECRET_TEST_CASES, name_func=custom_test_name_func
    )
    def test_people_aware_of_secret_dp(
        self, n: int, delay: int, forget: int, expected: int
    ):
        actual = people_aware_of_secret(n, delay, forget)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        PEOPLE_AWARE_OF_A_SECRET_TEST_CASES, name_func=custom_test_name_func
    )
    def test_people_aware_of_secret_simulation_deque(
        self, n: int, delay: int, forget: int, expected: int
    ):
        actual = people_aware_of_secret_simulation_deque(n, delay, forget)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
