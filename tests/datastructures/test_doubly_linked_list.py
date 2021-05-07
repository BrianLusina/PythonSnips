import unittest

from datastructures.linked_lists.doubly_linked_list import DoublyLinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.list = DoublyLinkedList()

    def test_push_pop(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(10, self.list.pop().data)

    def test_push_shift(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(10, self.list.shift())
        self.assertEqual(20, self.list.shift())

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(20, self.list.shift())
        self.assertEqual(10, self.list.shift())

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(10, self.list.pop().data)
        self.assertEqual(20, self.list.pop().data)

    def test_all(self):
        self.list.append(10)
        self.list.append(20)
        self.assertEqual(20, self.list.pop().data)
        self.list.append(30)
        self.assertEqual(10, self.list.shift())
        self.list.unshift(40)
        self.list.append(50)
        self.assertEqual(40, self.list.shift())
        self.assertEqual(50, self.list.pop().data)
        self.assertEqual(30, self.list.shift())


if __name__ == '__main__':
    unittest.main()
