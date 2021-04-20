import unittest

from pymath.reciprocal_cycles import longest_recurring_cycle


class ReciprocalCyclesTestCase(unittest.TestCase):
    def test_limit_8(self):
        self.assertEqual(7, longest_recurring_cycle(8))

    def test_limit_7(self):
        self.assertEqual(3, longest_recurring_cycle(7))

    def test_limit_10(self):
        self.assertEqual(7, longest_recurring_cycle(10))

    def test_raises_on_invalid_input(self):
        with self.assertRaises(ValueError):
            longest_recurring_cycle("10")

        with self.assertRaises(ValueError):
            longest_recurring_cycle(10.0)

        with self.assertRaises(ValueError):
            longest_recurring_cycle({})

    def test_limit_1000(self):
        self.assertEqual(983, longest_recurring_cycle(1000))

    def test_limit_2000(self):
        self.assertEqual(1979, longest_recurring_cycle(2000))

    def test_limit_2500(self):
        self.assertEqual(2473, longest_recurring_cycle(2500))

    def test_limit_10000(self):
        self.assertEqual(9967, longest_recurring_cycle(10000))

    def test_limit_25000(self):
        self.assertEqual(24989, longest_recurring_cycle(25000))

    @unittest.skip("Really long runtime")
    def test_limit_100000(self):
        self.assertEqual(99989, longest_recurring_cycle(100000))

    @unittest.skip("Really long runtime")
    def test_limit_1000000(self):
        self.assertEqual(999983, longest_recurring_cycle(100000))


if __name__ == '__main__':
    unittest.main()
