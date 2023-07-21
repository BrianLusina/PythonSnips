import unittest
from . import asteroid_collision


class AsteroidCollisionTestCase(unittest.TestCase):
    def test_one(self):
        """should return [5, 10] from [5, 10,-5]"""
        asteroids = [5, 10, -5]
        expected = [5, 10]
        actual = asteroid_collision(asteroids)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return [8, -8] from []"""
        asteroids = [8, -8]
        expected = []
        actual = asteroid_collision(asteroids)
        self.assertEqual(expected, actual)

    def test_three(self):
        """should return [10, 2, -5] from [10]"""
        asteroids = [10, 2, -5]
        expected = [10]
        actual = asteroid_collision(asteroids)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
