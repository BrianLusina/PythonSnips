import unittest
from . import SmallestInfiniteSet


class SmallestInfiniteSetTestCase(unittest.TestCase):
    def test_1(self):
        """add_back(2) -> pop_smallest() -> pop_smallest() -> pop_smallest() -> add_back(1) -> pop_smallest() -> pop_smallest() -> pop_smallest()"""
        smallest_infinite_set = SmallestInfiniteSet()

        # 2 is already in the set, so no change is made.
        smallest_infinite_set.add_back(2)

        # return 1, since 1 is the smallest number, and remove it from the set.
        actual1 = smallest_infinite_set.pop_smallest()
        expected1 = 1
        self.assertEqual(expected1, actual1)

        # return 2, and remove it from the set.
        actual2 = smallest_infinite_set.pop_smallest()
        expected2 = 2
        self.assertEqual(expected2, actual2)

        # return 3, and remove it from the set.
        actual3 = smallest_infinite_set.pop_smallest()
        expected3 = 3
        self.assertEqual(expected3, actual3)

        # 1 is added back to set
        smallest_infinite_set.add_back(1)

        # return 1, since 1 was added back to the set and is the smallest number, and remove it from the set.
        actual1_1 = smallest_infinite_set.pop_smallest()
        expected1_1 = 1
        self.assertEqual(expected1_1, actual1_1)

        # return 4, and remove it from the set.
        smallest_infinite_set.pop_smallest()

    def test_2(self):
        """pop_smallest() is called 1000 times should not error out"""
        smallest_infinite_set = SmallestInfiniteSet()

        for x in range(1, 1001):
            actual = smallest_infinite_set.pop_smallest()
            self.assertEqual(x, actual)


if __name__ == "__main__":
    unittest.main()
