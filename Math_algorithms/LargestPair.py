import unittest
import heapq


class MaxProd(object):
    def __init__(self, array):
        self.array = array

    # slowest implementation
    def max_product_slow(self):
        n = sorted(self.array, reverse=True)
        return n[0] * n[1]

    # average of the three solutions
    def max_product_avg(self):
        count = 0
        m1 = m2 = float('-inf')
        for x in self.array:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1
                else:
                    m2 = x
        return m1 * m2

    # faster solution
    def max_product_fast(self):
        first = max(self.array)
        second = max(n for n in self.array if n != first)
        return first *  second

    def max_product_fastest(self):
        x = heapq.nlargest(2, self.array)
        return x[0] * x[1]


# fastest solution
def max_product(array):
    first = max(array)
    second = max(n for n in array if n != first)
    return second * first


class LargestPairTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_product([56, 335, 195, 443, 6, 494, 252]), 218842)

    def test_2(self):
        self.assertEqual(max_product([154, 428, 455, 346]), 194740)

    def test_3(self):
        self.assertEqual(max_product([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411]), 187827)

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