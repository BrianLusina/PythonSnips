import unittest
from random import randint

from pytime.clock_in_mirror import what_is_the_time


class ClockTestCases(unittest.TestCase):
    def test_2(self):
        self.assertEqual(what_is_the_time("06:35"), "05:25", "didn't work for '06:35'")

    def test_3(self):
        self.assertEqual(what_is_the_time("11:59"), "12:01", "didn't work for '11:59'")

    def test_4(self):
        self.assertEqual(what_is_the_time("12:02"), "11:58", "didn't work for '12:02'")

    def test_5(self):
        self.assertEqual(what_is_the_time("04:00"), "08:00", "didn't work for '04:00'")

    def test_6(self):
        self.assertEqual(what_is_the_time("06:00"), "06:00", "didn't work for '06:00'")

    def test_7(self):
        self.assertEqual(what_is_the_time("12:00"), "12:00", "didn't work for '12:00'")

    @staticmethod
    def rand_time():
        return "{:02}:{:02}".format(randint(1, 12), randint(0, 59))

    def test_random(self):
        for i in range(10):
            time = ClockTestCases.rand_time()
            self.assertEqual(what_is_the_time(what_is_the_time(time)), time, "didn't work for " + time)


if __name__ == '__main__':
    unittest.main()
