import unittest


"""
Perform validation on time string
Split it into the time components, convert each time component to an integer,
store time components in variables, hour for hour, minute for minutes and second for seconds
perform operations on each time component
if time component is not valid, return None
"""


def time_correct(time_string):
    result = []
    if time_string is None or len(time_string) < 8:
        return time_string
    elif time_string == "":
        return time_string
    else:
        these_times = time_string.split(":")
        for time_unit in these_times:
            hour, minute, second = these_times[0], these_times[1], these_times[2]
            if isinstance(int(hour), int):
                int(hour) < 24
            else:
                return None


class Tests(unittest.TestCase):
    def test2(self):
        self.assertEqual(time_correct(None), None)

    def test3(self):
        self.assertEqual(time_correct(""), "")

    def test4(self):
        self.assertEqual(time_correct("001122"), None)

    def test5(self):
        self.assertEqual(time_correct("00;11;22"), None)

    def test6(self):
        self.assertEqual(time_correct("0a:1c:22"), None)

    def test7(self):
        self.assertEqual(time_correct("09:10:01"), "09:10:01")

    def test8(self):
        self.assertEqual(time_correct("11:70:10"), "12:10:10")

    def test9(self):
        self.assertEqual(time_correct("19:99:99"), "20:40:39")

    def test10(self):
            self.assertEqual(time_correct("24:01:01"), "00:01:01")

    def test11(self):
        self.assertEqual(time_correct("52:01:01"), "04:01:01")