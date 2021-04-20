import unittest

from pymath.triangles.triangle_number import is_triangle_number


class TriangleNumberTests(unittest.TestCase):
    """
    Triangle Number test cases
    """

    def test_1(self):
        self.assertEqual(is_triangle_number(3), True, "Expected True for input 3. Got "
                         .join(str(is_triangle_number(3))).join("."))

    def test_2(self):
        self.assertEqual(is_triangle_number(5), False, "Expected False for input 5. Got "
                         .join(str(is_triangle_number(5))).join("."))

    def test_3(self):
        self.assertEqual(is_triangle_number("hello!"), False, "Expected False for input 'hello!'. Got "
                         .join(str(is_triangle_number("hello!"))).join("."))

    def test_4(self):
        self.assertEqual(is_triangle_number(6.15), False, "Expected False for input 6.15. Got "
                         .join(str(is_triangle_number(6.15))).join("."))


if __name__ == "__main__":
    unittest.main()
