import unittest
from math import sqrt

from pymath.triangles.triangle import Triangle, TriangleError


class TriangleTests(unittest.TestCase):
    def test_equilateral_triangles_have_equal_sides(self):
        self.assertEqual("equilateral", Triangle(2, 2, 2).kind())

    def test_larger_equilateral_triangles_also_have_equal_sides(self):
        self.assertEqual("equilateral", Triangle(10, 10, 10).kind())

    def test_isosceles_triangles_have_last_two_sides_equal(self):
        self.assertEqual("isosceles", Triangle(3, 4, 4).kind())

    def test_isosceles_triangles_have_first_and_last_sides_equal(self):
        self.assertEqual("isosceles", Triangle(4, 3, 4).kind())

    def test_isosceles_triangles_have_two_first_sides_equal(self):
        self.assertEqual("isosceles", Triangle(4, 4, 3).kind())

    def test_isosceles_triangles_have_in_fact_exactly_two_sides_equal(self):
        self.assertEqual("isosceles", Triangle(10, 10, 2).kind())

    def test_scalene_triangles_have_no_equal_sides(self):
        self.assertEqual("scalene", Triangle(3, 4, 5).kind())

    def test_scalene_triangles_have_no_equal_sides_at_a_larger_scale_too(self):
        self.assertEqual("scalene", Triangle(10, 11, 12).kind())

        self.assertEqual("scalene", Triangle(5, 4, 2).kind())

    def test_very_small_triangles_are_legal(self):
        self.assertEqual("scalene", Triangle(0.4, 0.6, 0.3).kind())

    def test_triangles_with_no_size_are_illegal(self):
        self.assertRaises(TriangleError, Triangle, 0, 0, 0)

    def test_triangles_with_negative_sides_are_illegal(self):
        self.assertRaises(TriangleError, Triangle, 3, 4, -5)

    def test_triangles_violating_triangle_inequality_are_illegal(self):
        self.assertRaises(TriangleError, Triangle, 1, 1, 3)

    def test_triangles_violating_triangle_inequality_are_illegal_2(self):
        self.assertRaises(TriangleError, Triangle, 2, 4, 2)

    def test_triangles_violating_triangle_inequality_are_illegal_3(self):
        self.assertRaises(TriangleError, Triangle, 7, 3, 2)

    def test_perimeter(self):
        self.assertEqual(Triangle(2, 2, 2).perimeter(), sum([2, 2, 2]))

    def test_area_equilateral(self):
        self.assertEqual(Triangle(3, 3, 3).area(), (sqrt(3) * pow(3, 2)) / 4)

    def test_area_isosceles(self):
        self.assertEqual(
            Triangle(2, 3, 3).area(),
            (0.5 * pow(2, 2)) * sqrt((pow(3, 2) / pow(2, 2)) - (1 / 4)),
        )

    def test_area_scalene(self):
        s = (2 + 3 + 4) / 2
        area = sqrt(s * (s - 2) * (s - 3) * (s - 4))
        self.assertEqual(Triangle(2, 3, 4).area(), area)


if __name__ == "__main__":
    unittest.main()
