import unittest
from random import randint

from pystrings.rgb_to_hex import rgb_to_hex


class RgbToHexTestCase(unittest.TestCase):

    @staticmethod
    def test_rgb(*args):
        return "".join(hex(min(255, max(0, x)))[2:].zfill(2).upper() for x in args)

    def test(self):
        self.assertEquals(rgb_to_hex(0, 0, 0), "000000", "testing zero values")
        self.assertEquals(rgb_to_hex(1, 2, 3), "010203", "testing near zero values")
        self.assertEquals(rgb_to_hex(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEquals(rgb_to_hex(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEquals(rgb_to_hex(-20, 275, 125), "00FF7D", "testing out of range values")

    def test_random(self):
        for _ in range(5):
            r = randint(0, 255) + (-1) ** randint(1, 2) * randint(0, 255)
            g = randint(0, 255) + (-1) ** randint(1, 2) * randint(0, 255)
            b = randint(0, 255) + (-1) ** randint(1, 2) * randint(0, 255)
            self.assertEquals(rgb_to_hex(r, g, b), self.test_rgb(r, g, b),
                              "Testing random values: " + " ,".join(map(str, [r, g, b])))


if __name__ == '__main__':
    unittest.main()
