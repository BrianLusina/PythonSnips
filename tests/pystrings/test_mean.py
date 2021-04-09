import unittest

from pystrings.mean import mean


class MeanTests(unittest.TestCase):
    def test_1(self):
        lst1 = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']
        self.assertEqual(mean(lst1), [3.6, 'udiwstagwo'])

    def test_2(self):
        lst2 = ['0', 'c', '7', 'x', '6', '2', '3', '5', 'w', '7', '0', 'y', 'v', 'u', 'h', 'i', 'n', 'u', '0', '0']
        self.assertEqual(mean(lst2), [3.0, 'cxwyvuhinu'])

    def test_3(self):
        lst3 = ['0', 'u', 'a', 'y', '0', 'a', '9', 'q', '3', 'v', 'g', '7', '6', '4', 'y', 'd', '8', '6', '0', 'd']
        self.assertEqual(mean(lst3), [4.3, 'uayaqvgydd'])

    def test_4(self):
        lst4 = ['s', 'n', '9', 'l', '0', 'm', 'i', 'z', '9', '7', 'y', '4', 'z', '3', '3', 'k', '4', '1', '0', 'k']
        self.assertEqual(mean(lst4), [4.0, 'snlmizyzkk'])

    def test_5(self):
        lst5 = ['5', 'v', 'u', 'k', '8', '4', '9', 'b', '9', 'g', '5', 'z', '3', 'f', '6', 'u', 'i', '6', '6', 't']
        self.assertEqual(mean(lst5), [6.1, 'vukbgzfuit'])
