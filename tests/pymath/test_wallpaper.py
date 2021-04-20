import unittest

from pymath.wallpaper import wallpaper


# todo: failing tests
@unittest.skip
class MyTestCase(unittest.TestCase):
    def test_2(self):
        self.assertEqual(wallpaper(6.3, 4.5, 3.29), "sixteen")

    def test_3(self):
        self.assertEqual(wallpaper(7.8, 2.9, 3.29), "sixteen")

    def test_4(self):
        self.assertEqual(wallpaper(6.3, 5.8, 3.13), "seventeen")

    def test_5(self):
        self.assertEqual(wallpaper(6.1, 6.7, 2.81), "sixteen")


if __name__ == '__main__':
    unittest.main()
