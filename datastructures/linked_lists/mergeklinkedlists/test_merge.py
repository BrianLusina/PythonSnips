import unittest
from . import merge_two_sorted_lists
from ..singly_linked_list import SinglyLinkedList


class MergeSortedLinkedListsTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 from l1=[1,5,6,8] and l2=[2,3,4,7]"""
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        l1 = [1, 5, 6, 8]
        linked_list_one = SinglyLinkedList()
        for data in l1:
            linked_list_one.append(data)

        l2 = [2, 3, 4, 7]
        linked_list_two = SinglyLinkedList()
        for data in l2:
            linked_list_two.append(data)

        actual = merge_two_sorted_lists(linked_list_one.head, linked_list_two.head)
        self.assertIsNotNone(actual)

        actual_head = actual
        actual_data = []
        while actual_head:
            actual_data.append(actual_head.data)
            actual_head = actual_head.next

        self.assertEqual(expected, actual_data)


if __name__ == '__main__':
    unittest.main()
