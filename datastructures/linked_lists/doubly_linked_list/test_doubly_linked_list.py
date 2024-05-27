import unittest

from . import DoublyLinkedList


class DoublyLinkedListAppendPrependTests(unittest.TestCase):
    def test_append(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(10)
        doubly_linked_list.append(20)

        self.assertEqual(2, len(doubly_linked_list))

    def test_prepend(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(10)
        doubly_linked_list.append(20)

        self.assertEqual(2, len(doubly_linked_list))

        doubly_linked_list.prepend(30)
        doubly_linked_list.prepend(40)

        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(40, doubly_linked_list.head.data)


class DoublyLinkedListInsertAfterAndBeforeNodeTests(unittest.TestCase):
    def test_insert_e_after_b(self):
        """Should insert E after B in list A-B-C-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("B")
        new_data = "E"

        doubly_linked_list.insert_after_node(key, new_data)
        expected = ["A", "B", new_data, "C", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_insert_e_before_b(self):
        """Should insert E before B in list A-B-C-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("B")
        new_data = "E"

        doubly_linked_list.insert_before_node(key, new_data)
        expected = ["A", new_data, "B", "C", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))


class DoublyLinkedListTests(unittest.TestCase):
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
