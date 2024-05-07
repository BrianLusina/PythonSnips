import unittest

from . import SinglyLinkedList


class LinkedListIsPalindromeTestCase(unittest.TestCase):
    def test_1(self):
        """should move tail of ["r", "a", "c", "e", "c", "a", "r"] to become ["r", "r", "a", "c", "e", "c", "a"]"""
        linked_list = SinglyLinkedList()
        data = ["r", "a", "c", "e", "c", "a", "r"]
        expected = ["r", "r", "a", "c", "e", "c", "a"]
        expected_head = "r"

        for d in data:
            linked_list.append(d)

        linked_list.move_tail_to_head()
        actual_head = linked_list.head

        self.assertIsNotNone(actual_head)
        self.assertEqual(expected_head, actual_head.data)

        actual_data = []
        while actual_head:
            actual_data.append(actual_head.data)
            actual_head = actual_head.next

        self.assertEqual(expected, actual_data)

    def test_2(self):
        """should move tail of ["a", "b", "c", "d"] to become ["d", "a", "b", "c"]"""
        linked_list = SinglyLinkedList()
        data = ["a", "b", "c", "d"]
        expected = ["d", "a", "b", "c"]
        expected_head = "d"

        for d in data:
            linked_list.append(d)

        linked_list.move_tail_to_head()
        actual_head = linked_list.head

        self.assertIsNotNone(actual_head)
        self.assertEqual(expected_head, actual_head.data)

        actual_data = []
        while actual_head:
            actual_data.append(actual_head.data)
            actual_head = actual_head.next

        self.assertEqual(expected, actual_data)


if __name__ == "__main__":
    unittest.main()
