import unittest

from datastructures.lfucache import LFUCache


class LFUCacheTestCases(unittest.TestCase):
    def test_with_capacity_of_2(self):
        lfucache = LFUCache(2)

        lfucache.put(1, 1)
        self.assertEquals(1, lfucache._current_size)

        lfucache.put(2, 2)
        self.assertEquals(2, lfucache._current_size)

        value_one = lfucache.get(1)
        self.assertEquals(1, value_one)

        lfucache.put(3, 3)
        value_two_not_found = lfucache.get(2)
        self.assertIsNone(value_two_not_found)

        value_3 = lfucache.get(3)
        self.assertEquals(3, value_3)

        lfucache.put(4, 4)
        value_one_not_found = lfucache.get(1)
        self.assertIsNone(value_one_not_found)

        value_3_two = lfucache.get(3)
        self.assertEquals(3, value_3_two)

        value_4 = lfucache.get(4)
        self.assertEquals(4, value_4)


if __name__ == '__main__':
    unittest.main()
