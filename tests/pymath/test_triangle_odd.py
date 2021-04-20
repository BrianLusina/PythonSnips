import time
import unittest

from pymath.triangles.triangle_odd import row_sum_odd_numbers


class TriangleTests(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_1(self):
        time.sleep(1)
        self.assertEquals(row_sum_odd_numbers(1), 1)

    def test_2(self):
        time.sleep(2)
        self.assertEquals(row_sum_odd_numbers(2), 8)

    def test_3(self):
        time.sleep(3)
        self.assertEquals(row_sum_odd_numbers(13), 2197)

    def test_4(self):
        time.sleep(4)
        self.assertEquals(row_sum_odd_numbers(19), 6859)

    def test_5(self):
        time.sleep(5)
        self.assertEquals(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TriangleTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
