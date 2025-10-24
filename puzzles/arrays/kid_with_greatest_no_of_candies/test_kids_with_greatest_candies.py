import unittest

from . import kids_with_candies


class KidsWithGreatestNumberOfCandiesTestCase(unittest.TestCase):
    def test_one(self):
        """should return [true,true,true,false,true] for candies=[2,3,5,1,3] and extra_candies=3"""
        expected = [True, True, True, False, True]
        candies = [2, 3, 5, 1, 3]
        extra_candies = 3
        actual = kids_with_candies(candies=candies, extra_candies=extra_candies)

        self.assertEqual(expected, actual)

    def test_two(self):
        """should return [true,false,false,false,false] for candies=[4,2,1,1,2] and extra_candies=1"""
        expected = [True, False, False, False, False]
        candies = [4, 2, 1, 1, 2]
        extra_candies = 1
        actual = kids_with_candies(candies=candies, extra_candies=extra_candies)

        self.assertEqual(expected, actual)

    def test_three(self):
        """should return [true,false,true] for candies=[12,1,12] and extra_candies=10"""
        expected = [True, False, True]
        candies = [12, 1, 12]
        extra_candies = 10
        actual = kids_with_candies(candies=candies, extra_candies=extra_candies)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
