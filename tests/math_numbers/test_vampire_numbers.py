import unittest
from pysnips.math_numbers.vampire_numbers import VampireNumbers


class VampireTestCases(unittest.TestCase):
    def setUp(self):
        self.vampire_numbers = VampireNumbers()

    def test_can_generate_first_25_vampire_numbers(self):
        print('First 15 vampire numbers')
        count = n = 0
        results = []
        while count < 15:
            n += 1
            fang_pairs = self.vampire_numbers.vampire(n)
            if fang_pairs:
                count += 1
                results.append((n, fang_pairs))

        self.assertEqual(15, len(results), "Expected 1st 25 vampire numbers")

    def test1(self):
        self.assertEqual(self.vampire_numbers.vampire_test(21, 6), True, "Basic: 21 * 6 = 126 should return True")

    def test2(self):
        self.assertEqual(self.vampire_numbers.vampire_test(204, 615), True, "Basic: 204 * 615 = 125460 should return "
                                                                            "True")

    def test3(self):
        self.assertEqual(self.vampire_numbers.vampire_test(30, -51), True, "One Negative: 30 * -51 = -1530 should "
                                                                           "return True")

    def test4(self):
        self.assertEqual(self.vampire_numbers.vampire_test(-246, -510), False,
                         "Double Negatives: -246 * -510 = 125460 should "
                         "return False (The negative signs aren't present "
                         "on the product)")

    def test5(self):
        self.assertEqual(self.vampire_numbers.vampire_test(210, 600), True,
                         "Trailing Zeroes: 210 * 600 = 126000 should return True")

    def test6(self):
        self.assertEqual(self.vampire_numbers.vampire_test(2947051, 8469153), False, "Should return false")

    def test7(self):
        self.assertEqual(self.vampire_numbers.vampire_test(0, 0), False, "Zeroes")

    def test8(self):
        self.assertEqual(self.vampire_numbers.vampire_test(11, 11), False, "Elevens")

    def test9(self):
        self.assertEqual(self.vampire_numbers.vampire_test(10, 1), False, "Identity")

    def test10(self):
        self.assertEqual(self.vampire_numbers.vampire_test(10, 11), False, "Missing 1, Result is 110")


if __name__ == "__main__":
    unittest.main()
