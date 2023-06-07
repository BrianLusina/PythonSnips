import unittest

from . import DoublyLinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_push_pop(self):
        self.list.append(10)
        self.list.append(20)

        self.assertEqual(2, len(self.list))

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(1, len(self.list))

        self.assertEqual(10, self.list.pop().data)
        self.assertEqual(0, len(self.list))

    def test_push_shift(self):
        self.list.append(10)
        self.list.append(20)

        self.assertEqual(2, len(self.list))

        self.assertEqual(10, self.list.shift())
        self.assertEqual(1, len(self.list))

        self.assertEqual(20, self.list.shift())
        self.assertEqual(0, len(self.list))

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(2, len(self.list))

        self.assertEqual(20, self.list.shift())
        self.assertEqual(1, len(self.list))

        self.assertEqual(10, self.list.shift())
        self.assertEqual(0, len(self.list))

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(2, len(self.list))

        self.assertEqual(10, self.list.pop().data)
        self.assertEqual(1, len(self.list))

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(0, len(self.list))

    def test_all(self):
        # list is []
        self.assertEqual(0, len(self.list))

        self.list.append(10)
        self.assertEqual(1, len(self.list))
        # list is 10->None

        self.list.append(20)
        self.assertEqual(2, len(self.list))
        # list is 10<->20->None

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(1, len(self.list))
        # list is 10<->None

        self.list.append(30)
        self.assertEqual(2, len(self.list))
        # list is 10<->30->None

        self.assertEqual(10, self.list.shift())
        self.assertEqual(1, len(self.list))
        # list is 30->None

        self.list.unshift(40)
        self.assertEqual(2, len(self.list))
        # list is 40<->30->None

        self.list.append(50)
        self.assertEqual(3, len(self.list))
        # list is 40<->30<->50->None

        self.assertEqual(40, self.list.shift())
        self.assertEqual(2, len(self.list))
        # list is 30<->50->None

        self.assertEqual(50, self.list.pop().data)
        self.assertEqual(1, len(self.list))
        # list is 30->None

        self.assertEqual(30, self.list.shift())
        self.assertEqual(0, len(self.list))
        # list is []


if __name__ == "__main__":
    unittest.main()
