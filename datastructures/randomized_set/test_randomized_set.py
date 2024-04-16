import unittest
from . import RandomizedSet


class RandomizedSetTestCase(unittest.TestCase):
    def test_1(self):
        """ "test steps insert(1) -> remove(2) -> insert(2) -> get_random() -> remove(1) -> insert(2) -> get_random()"""
        randomized_set = RandomizedSet()

        # Inserts 1 to the set. Returns true as 1 was inserted successfully
        actual_step_1 = randomized_set.insert(1)
        self.assertTrue(actual_step_1)

        # Returns false as 2 does not exist in the set.
        actual_step_2 = randomized_set.remove(2)
        self.assertFalse(actual_step_2)

        # Inserts 2 to the set, returns true. Set now contains [1,2].
        actual_step_3 = randomized_set.insert(2)
        self.assertTrue(actual_step_3)

        # getRandom() should return either 1 or 2 randomly.
        actual_step_4 = randomized_set.get_random()
        self.assertIn(actual_step_4, [1, 2])

        # Removes 1 from the set, returns true. Set now contains [2].
        actual_step_5 = randomized_set.remove(1)
        self.assertTrue(actual_step_5)

        # 2 was already in the set, so return false.
        actual_step_6 = randomized_set.insert(2)
        self.assertFalse(actual_step_6)

        # Since 2 is the only number in the set, getRandom() will always return 2.
        actual_step_7 = randomized_set.get_random()
        expected = 2
        self.assertEqual(expected, actual_step_7)


if __name__ == "__main__":
    unittest.main()
