import unittest
from design_patterns.hashmap import HashMap, Item


class HashMapTestCases(unittest.TestCase):
    def test_hashmap_with_size_of_3_adds_items(self):
        hashmap = HashMap(3)

        item_1 = 1, "something"
        hashmap.set(item_1[0], item_1[1])

        expected_item_1 = Item(item_1[0], item_1[1])
        actual_1 = hashmap.table[1][0]
        self.assertEqual(actual_1.key, expected_item_1.key)
        self.assertEqual(actual_1.data, expected_item_1.data)

        item_2 = 2, "something"
        hashmap.set(item_2[0], item_2[1])

        expected_item_2 = Item(item_2[0], item_2[1])
        actual_2 = hashmap.table[2][0]
        self.assertEqual(actual_2.key, expected_item_2.key)
        self.assertEqual(actual_2.data, expected_item_2.data)

        item_3 = 3, "something"
        hashmap.set(item_3[0], item_3[1])

        expected_item_3 = Item(item_3[0], item_3[1])
        actual_3 = hashmap.table[0][0]
        self.assertEqual(actual_3.key, expected_item_3.key)
        self.assertEqual(actual_3.data, expected_item_3.data)

        item_4 = 4, "something"
        hashmap.set(item_4[0], item_4[1])

        expected_item_4 = Item(item_4[0], item_4[1])
        actual_4 = hashmap.table[1][1]
        self.assertEqual(actual_4.key, expected_item_4.key)
        self.assertEqual(actual_4.data, expected_item_4.data)

        # can handle collisions

        item_5 = 2, "something"
        hashmap.set(item_5[0], item_5[1])

        expected_item_5 = Item(item_5[0], item_5[1])
        actual_5 = hashmap.table[2][0]
        self.assertEqual(actual_5.key, expected_item_5.key)
        self.assertEqual(actual_5.data, expected_item_5.data)

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
        self.assertRaises(KeyError, hashmap.remove, 10)
        self.assertRaises(KeyError, hashmap.remove, 0)

        # removes items by keys

        # check that the length is 2 for the key position we want to remove
        self.assertEqual(2, len(hashmap.table[1]))

        # remove key
        hashmap.remove(1)

        # this will indicate the item no longer exists at this position
        self.assertEqual(1, len(hashmap.table[1]))

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


if __name__ == '__main__':
    unittest.main()
