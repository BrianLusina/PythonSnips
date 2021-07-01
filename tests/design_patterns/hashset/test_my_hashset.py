import unittest

from design_patterns.hashset import MyHashSet


class MyHashSetTestCase(unittest.TestCase):
    hashset = MyHashSet()

    def test_add_1(self):
        self.hashset.add(1)
        self.assertEqual(self.hashset.map[1], True)

    def test_add_2(self):
        self.hashset.add(2)
        self.assertEqual(self.hashset.map[2], True)

    def test_contains_1(self):
        actual = self.hashset.contains(1)
        self.assertTrue(actual)

    def test_contains_3(self):
        actual = self.hashset.contains(3)
        self.assertFalse(actual)

    def test_add_another_2(self):
        self.hashset.add(2)
        self.assertEqual({1: True, 2: True}, self.hashset.map)
        self.assertEqual(self.hashset.map[2], True)

    def test_contains_2(self):
        actual = self.hashset.contains(2)
        self.assertTrue(actual)

    def test_remove_2(self):
        self.hashset.remove(2)
        self.assertEqual({1: True}, self.hashset.map)
        actual = self.hashset.contains(2)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
