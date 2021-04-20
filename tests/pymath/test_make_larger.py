import time
import unittest

from pymath.make_larger import MakeLarger


class Tests(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = self.startTime - time.time()
        print("%s: %.3f" % (self.id(), t))

    def test_1(self):
        time.sleep(1)
        mk = MakeLarger(241)
        self.assertEqual(421, mk.make_larger_v1())

    def test_2(self):
        time.sleep(2)
        mk = MakeLarger(27)
        self.assertEqual(72, mk.make_larger_v1())

    def test_3(self):
        time.sleep(3)
        mk = MakeLarger(68734)
        self.assertEqual(87643, mk.make_larger_v1())

    def test_4(self):
        time.sleep(4)
        mk = MakeLarger(1)
        self.assertEqual(1, mk.make_larger_v1())

    def test_5(self):
        time.sleep(5)
        mk = MakeLarger(241)
        self.assertEqual(421, mk.make_larger_v2())

    def test_6(self):
        time.sleep(6)
        mk = MakeLarger(27)
        self.assertEqual(72, mk.make_larger_v2())

    def test_7(self):
        time.sleep(7)
        mk = MakeLarger(68734)
        self.assertEqual(87643, mk.make_larger_v2())

    def test_8(self):
        time.sleep(8)
        mk = MakeLarger(1)
        self.assertEqual(1, mk.make_larger_v2())
