import unittest

from pymath.largest_pair import max_product


class LargestPairTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_product([56, 335, 195, 443, 6, 494, 252]), 218842)

    def test_2(self):
        self.assertEqual(max_product([154, 428, 455, 346]), 194740)

    def test_3(self):
        self.assertEqual(max_product([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411]),
                         187827)

    def test_4(self):
        self.assertEqual(max_product([136, 376, 10, 146, 105, 63, 234]), 87984)

    def test_5(self):
        self.assertEqual(max_product([354, 463, 165, 62, 472, 53, 347, 293, 252, 378, 420, 398, 255, 89]), 218536)

    def test_6(self):
        self.assertEqual(max_product([346, 446, 26, 425, 432, 349, 123, 269, 285, 93, 75, 14]), 192672)

    def test_7(self):
        self.assertEqual(max_product([134, 320, 266, 299]), 95680)

    def test_8(self):
        self.assertEqual(max_product([114, 424, 53, 272, 128, 215, 25, 329, 272, 313, 100, 24, 252]), 139496)

    def test_9(self):
        self.assertEqual(max_product([375, 56, 337, 466, 203]), 174750)
