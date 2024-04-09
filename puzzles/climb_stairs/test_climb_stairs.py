import unittest

from . import climb_stairs


class ClimbStairsTestCase(unittest.TestCase):
    def test_1(self):
        """should return 2 for n = 2"""
        n = 2
        expected = 2
        actual = climb_stairs(n)

        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 3 for n = 3"""
        n = 3
        expected = 3
        actual = climb_stairs(n)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
