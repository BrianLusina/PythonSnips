import unittest
from math import pi, sqrt, acos, floor
from random import randint

from pymath.tank_truck import tankvol


def tankvol_sol(h, d, vt):
    if h == 0:
        return 0
    r = d / 2.0
    if h == r:
        return vt // 2
    if h == d:
        return vt
    if h > r:
        h = d - h
        hilevel = True
    else:
        hilevel = False
    st = pi * r * r
    theta = acos((r - h) / r)
    sr = (r - h) * sqrt(r * r - (r - h) ** 2)
    sa = st / pi * theta
    sh = sa - sr
    v = vt * sh / st
    if hilevel:
        v = vt - v
    return int(floor(v))


class TankTankTestCase(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(tankvol(5, 7, 3848), 2940)
        self.assertEqual(tankvol(2, 7, 3848), 907)
        self.assertEqual(tankvol(2, 8, 5026), 982)
        self.assertEqual(tankvol(4, 9, 6361), 2731)
        self.assertEqual(tankvol(3, 10, 7853), 1981)
        self.assertEqual(tankvol(3, 5, 1963), 1229)
        self.assertEqual(tankvol(5, 7, 3848), 2940)
        self.assertEqual(tankvol(4, 7, 3848), 2272)
        self.assertEqual(tankvol(0, 7, 3848), 0)
        self.assertEqual(tankvol(7, 7, 3848), 3848)

        self.assertEqual(tankvol(2, 5, 1963), 733)
        self.assertEqual(tankvol(2, 4, 1256), 628)
        self.assertEqual(tankvol(4, 10, 7853), 2933)
        self.assertEqual(tankvol(3, 9, 6361), 1856)
        self.assertEqual(tankvol(2, 10, 7853), 1118)
        self.assertEqual(tankvol(5, 9, 6361), 3629)
        self.assertEqual(tankvol(5, 6, 2827), 2517)
        self.assertEqual(tankvol(1, 4, 1256), 245)

    def test_random(self):
        for _ in range(0, 100):
            h = randint(1, 5)
            d = randint(h + 1, 10)
            v = int(pi * (d / 2.0) * (d / 2.0) * 100.0)
            self.assertEqual(tankvol(h, d, v), tankvol_sol(h, d, v))


if __name__ == '__main__':
    unittest.main()
