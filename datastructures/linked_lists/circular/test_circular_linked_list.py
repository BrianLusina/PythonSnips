import unittest
from . import CircularLinkedList


class CircularLinkedListAppendTestCase(unittest.TestCase):
    def test_1(self):
        """should append a new node 7 to linked list [1,2,3,4,5,6] to become [1,2,3,4,5,6,7]"""
        data = [1, 2, 3, 4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6, 7]
        linked_list = CircularLinkedList()

        for d in data:
            linked_list.append(d)

        linked_list.append(7)

        actual_head = linked_list.head
        self.assertIsNotNone(actual_head)

        self.assertEqual(1, actual_head.data)
        self.assertEqual(expected, list(linked_list))


class CircularLinkedListPrependTestCase(unittest.TestCase):
    def test_1(self):
        """should prepend a new node 7 to linked list [1,2,3,4,5,6] to become [7,1,2,3,4,5,6]"""
        data = [1, 2, 3, 4, 5, 6]
        expected = [7, 1, 2, 3, 4, 5, 6]
        linked_list = CircularLinkedList()

        for d in data:
            linked_list.append(d)

        linked_list.prepend(7)

        actual_head = linked_list.head
        self.assertIsNotNone(actual_head)

        self.assertEqual(7, actual_head.data)
        self.assertEqual(expected, list(linked_list))


class CircularLinkedListDeleteNodeByKeyTestCase(unittest.TestCase):
    def test_1(self):
        """should delete a node 5 from linked list [1,2,3,4,5,6] to become [1,2,3,4,6]"""
        data = [1, 2, 3, 4, 5, 6]
        expected = [1, 2, 3, 4, 6]
        circular_linked_list = CircularLinkedList()

        for d in data:
            circular_linked_list.append(d)

        circular_linked_list.delete_node_by_key(5)

        self.assertEqual(expected, list(circular_linked_list))


class CircularLinkedListSplitListTestCase(unittest.TestCase):
    def test_1(self):
        """should split a linked list [1,2,3,4,5,6] to become ([1,2,3],[4,5,6])"""
        data = [1, 2, 3, 4, 5, 6]
        expected = ([1, 2, 3], [4, 5, 6])
        circular_linked_list = CircularLinkedList()

        for d in data:
            circular_linked_list.append(d)

        first_list, second_list = circular_linked_list.split_list()

        self.assertEqual(expected[0], list(first_list))
        self.assertEqual(expected[1], list(second_list))


if __name__ == '__main__':
    unittest.main()
