import unittest

from pytime.time_degrees import clock_degree


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(clock_degree("01:01"), "30:6")

    def test2(self):
        self.assertEqual(clock_degree("00:00"), "360:360")

    def test3(self):
        self.assertEqual(clock_degree("01:03"), "30:18")

    def test4(self):
        self.assertEqual(clock_degree("01:30"), "30:180")

    def test5(self):
        self.assertEqual(clock_degree("12:05"), "360:30")

    def test6(self):
        self.assertEqual(clock_degree("26:78"), "Check your time !")

    def test7(self):
        self.assertEqual(clock_degree("16:25"), "120:150")

    def test8(self):
        self.assertEqual(clock_degree("17:09"), "150:54")

    def test9(self):
        self.assertEqual(clock_degree("19:00"), "210:360")

    def test10(self):
        self.assertEqual(clock_degree("20:34"), "240:204")

    def test11(self):
        self.assertEqual(clock_degree("23:20"), "330:120")

    def test12(self):
        self.assertEqual(clock_degree("24:00"), "Check your time !")

    def test13(self):
        self.assertEqual(clock_degree("-09:00"), "Check your time !")
