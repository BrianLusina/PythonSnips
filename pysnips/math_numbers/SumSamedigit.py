import unittest


def sum_same(num, times):
    c, total = 1, 0
    while c <= times:
        n = str(num) * c
        total += int(n)
        c += 1
    return total


class SumSameDigTests(unittest.TestCase):
    def test_9(self):
        self.assertEqual(11106, sum_same(9, 4))
