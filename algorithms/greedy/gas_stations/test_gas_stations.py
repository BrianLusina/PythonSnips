import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.gas_stations import can_complete_circuit


class CanCompleteCircuitTestCase(unittest.TestCase):
    @parameterized.expand([
        ([1,2,3,4,5],[3,4,5,1,2],3),
        ([2,3,4],[3,4,3],-1),
        ([1, 2],[2,1],1),
    ])
    def test_can_complete_circuit(self, gas: List[int], cost: List[int], expected: int):
        actual = can_complete_circuit(gas, cost)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
