import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.gas_stations import can_complete_circuit

CAN_COMPLETE_CIRCUIT_TEST_CASES = [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([1, 2], [2, 1], 1),
    ([5, 2, 0, 3, 3], [1, 5, 5, 1, 1], 3),
]


class CanCompleteCircuitTestCase(unittest.TestCase):
    @parameterized.expand(CAN_COMPLETE_CIRCUIT_TEST_CASES)
    def test_can_complete_circuit(self, gas: List[int], cost: List[int], expected: int):
        actual = can_complete_circuit(gas, cost)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
