import unittest

from datastructures.hashmap.hash_map import HashMap


class HashMapTestCases(unittest.TestCase):
    def test_hashmap_with_size_of_3_adds_items(self):
        hashmap = HashMap(3)

        item_1_key = 1
        item_1_value = "something"
        hashmap.set(item_1_key, item_1_value)

        item_2_key = 2
        item_2_value = "something"
        hashmap.set(item_2_key, item_2_value)

        item_3_key = 3
        item_3_value = "something"
        hashmap.set(item_3_key, item_3_value)

        item_4_key = 4
        item_4_value = "something"
        hashmap.set(item_4_key, item_4_value)

        # can handle collisions

        item_5_key = 2
        item_5_value = "something"
        hashmap.set(item_5_key, item_5_value)

        actual_5 = hashmap.get(item_5_key)
        self.assertEqual(actual_5, item_5_value)

    def test_hashmap_can_remove_items(self):
        hashmap = HashMap(3)

        item_1 = 1, "something 1"
        item_2 = 2, "something 2"
        item_3 = 3, "something 3"
        item_4 = 4, "something 4"
        item_5 = 5, "something 5"

        hashmap.set(item_1[0], item_1[1])
        hashmap.set(item_2[0], item_2[1])
        hashmap.set(item_3[0], item_3[1])
        hashmap.set(item_4[0], item_4[1])
        hashmap.set(item_5[0], item_5[1])

        # raises KeyError for non existent keys
        self.assertRaises(KeyError, hashmap.get, 10)
        self.assertRaises(KeyError, hashmap.get, 0)

        # remove key
        hashmap.remove(1)

        with self.assertRaises(KeyError):
            hashmap.get(1)

    def test_hashmap_can_add_items(self):
        hashmap = HashMap(3)

        item_1 = 1, "something 1"
        item_2 = 2, "something 2"
        item_3 = 3, "something 3"
        item_4 = 4, "something 4"
        item_5 = 5, "something 5"

        hashmap.set(item_1[0], item_1[1])
        hashmap.set(item_2[0], item_2[1])
        hashmap.set(item_3[0], item_3[1])
        hashmap.set(item_4[0], item_4[1])
        hashmap.set(item_5[0], item_5[1])

        # raises KeyError for non existent keys
        self.assertRaises(KeyError, hashmap.get, 10)
        self.assertRaises(KeyError, hashmap.get, 0)

        # gets items by keys

        self.assertEqual("something 1", hashmap.get(1))
        self.assertEqual("something 2", hashmap.get(2))
        self.assertEqual("something 3", hashmap.get(3))
        self.assertEqual("something 4", hashmap.get(4))
        self.assertEqual("something 5", hashmap.get(5))


if __name__ == "__main__":
    unittest.main()
