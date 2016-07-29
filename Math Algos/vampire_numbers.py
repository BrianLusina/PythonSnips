import unittest


def vampire_test(x, y):
    for i in str(x)+str(y):
        if i in str(x * y):return True
        else: return False


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(vampire_test(21, 6), True, "Basic: 21 * 6 = 126 should return True")

    def test2(self):
        self.assertEqual(vampire_test(204, 615), True, "Basic: 204 * 615 = 125460 should return True")

    def test3(self):
        self.assertEqual(vampire_test(30, -51), True, "One Negative: 30 * -51 = -1530 should return True")

    def test4(self):
        self.assertEqual(vampire_test(-246, -510), False, "Double Negatives: -246 * -510 = 125460 should return False (The negative signs aren't present on the product)")

    def test5(self):
        self.assertEqual(vampire_test(210, 600), True, "Trailing Zeroes: 210 * 600 = 126000 should return True")

