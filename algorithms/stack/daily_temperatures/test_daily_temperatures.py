import unittest
from . import daily_temperatures


class DailyTemperaturesTestCase(unittest.TestCase):
    def test_1(self):
        """should return [1,1,4,2,1,1,0,0] for [73, 74, 75, 71, 69, 72, 76, 73]"""
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        actual = daily_temperatures(temperatures)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [1,1,1,0] for [30,40,50,60]"""
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        actual = daily_temperatures(temperatures)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [1,1,0] for [30,60,90]"""
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]
        actual = daily_temperatures(temperatures)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
