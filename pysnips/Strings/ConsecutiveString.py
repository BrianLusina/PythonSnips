import unittest

class ConsecutiveString(object):
    def __init__(self, starr, k):
        self.starr = starr
        self.k = k

    def longest_consec(self):
        result = ""

        if 0 < self.k <= len(self.starr):
            for index in range(len(self.starr) - self.k + 1):
                s = ''.join(self.starr[index:index + self.k])
                if len(s) > len(result):
                    result = s

        return result


def longest_consec(starr, k):
    result = ""
    if 0 < k <= len(starr):
        for index in range(len(starr) - k + 1):
            s = ''.join(starr[index:index + k])
            if len(s) > len(result):
                result = s

    return result

class ConsecutiveTests(unittest.TestCase):
    def test_1(self):
        long_con = ConsecutiveString(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
        self.assertEqual("abigailtheta", long_con.longest_consec())

    def test_2(self):
        long_con = ConsecutiveString(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
        self.assertEqual("oocccffuucccjjjkkkjyyyeehh",  long_con.longest_consec())

    def test_3(self):
        long_con = ConsecutiveString([], 3)
        self.assertEqual("", long_con.longest_consec())

    def test_4(self):
        long_con = ConsecutiveString(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
        self.assertEqual("wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck", long_con.longest_consec())

    def test_5(self):
        long_con = ConsecutiveString(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2)
        self.assertEqual("wlwsasphmxxowiaxujylentrklctozmymu", long_con.longest_consec())

    def test_6(self):
        long_con = ConsecutiveString(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
        self.assertEqual("", long_con.longest_consec())

    def test_7(self):
        long_con = ConsecutiveString(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3)
        self.assertEqual("ixoyx3452zzzzzzzzzzzz", long_con.longest_consec())

    def test_8(self):
        long_con = ConsecutiveString(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15)
        self.assertEqual("", long_con.longest_consec())

    def test_9(self):
        long_con = ConsecutiveString(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0)
        self.assertEqual("", long_con.longest_consec())
