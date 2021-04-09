import unittest

from cryptography.key_pad_decode import decode


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decode("4103432323"), "6957678787")

    def test_2(self):
        self.assertEqual(decode("4103438970"), "6957672135")

    def test_3(self):
        self.assertEqual(decode("4104305768"), "6956750342")

    def test_4(self):
        self.assertEqual(decode("4102204351"), "6958856709")

    def test_5(self):
        self.assertEqual(decode("4107056043"), "6953504567")


if __name__ == '__main__':
    unittest.main()
