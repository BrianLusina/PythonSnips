import unittest

from puzzles.fuel_injection_perfection import fuel_injection_perfection


class FuelInjectionPerfectionTestCases(unittest.TestCase):
    def test_input_of_4_returns_2(self):
        """input of '4' returns 2"""
        n = '4'
        expected = 2
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)

    def test_input_of_15_returns_5(self):
        """input of '15' returns 5"""
        n = '15'
        expected = 5
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)

    def test_input_of_13_returns_5(self):
        """input of '13' returns 5"""
        n = '13'
        expected = 5
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)

    def test_input_of_9_returns_4(self):
        """input of '9' returns 4"""
        n = '9'
        expected = 4
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)

    def test_input_of_2_returns_1(self):
        """input of '2' returns 1"""
        n = '2'
        expected = 1
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)

    def test_input_of_1_returns_0(self):
        """input of '1' returns 0"""
        n = '1'
        expected = 0
        actual = fuel_injection_perfection(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
