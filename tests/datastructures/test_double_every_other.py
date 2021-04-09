import unittest

from datastructures.lists.double_every_other import double_every_other


class DoubleTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual([1, 4, 3, 8, 5], double_every_other([1, 2, 3, 4, 5]))

    def test_two(self):
        self.assertEqual([1, 38, 6, 4, 12, -6], double_every_other([1, 19, 6, 2, 12, -3]))

    def test_three(self):
        self.assertEqual([-1000, 3306, 210, 0, 1], double_every_other([-1000, 1653, 210, 0, 1]))

    def test_4(self):
        self.assertEqual([-1278, 2276, 1617, 9076, -73, 7188, -1571, 2392, -46, 9856],
                         double_every_other([-1278, 1138, 1617, 4538, -73, 3594, -1571, 1196, -46, 4928]))

    def test_5(self):
        self.assertEqual(
            [-2967, -10228, 2691, 1536, -2816, -6216, -730, 2960, -447, -9796, 2896, -3264, 46, 304, 2716, 5928, -1071,
             1628, 2199, -10048, 591, -11096, 2877, 11720], double_every_other(
                [-2967, -5114, 2691, 768, -2816, -3108, -730, 1480, -447, -4898, 2896, -1632, 46, 152, 2716, 2964,
                 -1071, 814, 2199, -5024, 591, -5548, 2877, 5860]))

    def test_6(self):
        self.assertEqual([1802, 6272, -148, -10812, 700, 6272, -484],
                         double_every_other([1802, 3136, -148, -5406, 700, 3136, -484]))

    def test_7(self):
        self.assertEqual(
            [-732, 6396, -1943, 3560, -2290, -8344, -1636, 2004, 555, 4488, -146, -3460, 1458, 11168, -232, 8936, 1071,
             -1296, -453, 9280, 2069], double_every_other(
                [-732, 3198, -1943, 1780, -2290, -4172, -1636, 1002, 555, 2244, -146, -1730, 1458, 5584, -232, 4468,
                 1071, -648, -453, 4640, 2069]))

    def test_8(self):
        self.assertEqual([2373, -6852, 510], double_every_other([2373, -3426, 510]))
