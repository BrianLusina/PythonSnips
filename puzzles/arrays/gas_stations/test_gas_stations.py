import unittest

from . import can_complete_circuit


class CanCompleteCircuitTestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 for gas = (1, 2, 3, 4, 5), cost = (3, 4, 5, 1, 2)"""
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        actual = can_complete_circuit(gas, cost)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return -1 for gas = (2, 3, 4), cost = (3, 4, 3)"""
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        actual = can_complete_circuit(gas, cost)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
