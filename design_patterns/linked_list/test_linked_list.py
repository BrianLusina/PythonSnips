import unittest

from . import LinkedList


class LinkedListTestCases(unittest.TestCase):
    def test_return_negative_one_for_invalid_index_on_get(self):
        """Test return -1 on invalid index when using get(index)"""
        linked_list = LinkedList()

        actual = linked_list.get(-10)
        self.assertEqual(-1, actual)

    def test_return_negative_one_for_valid_index_on_get_but_no_head(self):
        """Test return -1 on valid index when using get(index) but there is not head"""
        linked_list = LinkedList()

        actual = linked_list.get(10)
        self.assertEqual(-1, actual)

    def test_return_negative_one_for_valid_index_on_get_with_head_but_no_next(self):
        """Test return -1 on valid index when using get(index) with valid head but no next node"""
        linked_list = LinkedList()

        linked_list.addAtHead(1)

        actual = linked_list.get(10)
        self.assertEqual(-1, actual)

    def test_return_value_for_valid_index_on_get_with_only_head(self):
        """Test return value on valid index when using get(index) with only head"""
        linked_list = LinkedList()

        linked_list.addAtHead(1)

        actual = linked_list.get(0)
        self.assertEqual(1, actual)

    def test_return_values_for_valid_indices_on_get_with_2_nodes(self):
        """Test return value on valid indices when using get(index) with 2 nodes"""
        linked_list = LinkedList()

        linked_list.addAtHead(1)
        linked_list.addAtHead(2)  # linked list is now 2 -> 1

        actual_zero = linked_list.get(0)
        self.assertEqual(2, actual_zero)

        actual_one = linked_list.get(1)
        self.assertEqual(1, actual_one)

    def test_one(self):
        """Test addAtHead -> addAtTail -> addAtIndex -> get -> deleteAtIndex -> get"""
        linked_list = LinkedList()

        linked_list.addAtHead(1)
        linked_list.addAtTail(3)
        linked_list.addAtIndex(1, 2)  # linked list becomes 1->2->3
        actual_two = linked_list.get(1)  # return 2
        self.assertEqual(2, actual_two)

        linked_list.deleteAtIndex(1)  # now the linked list is 1->3
        actual_three = linked_list.get(1)  # return 3
        self.assertEqual(3, actual_three)


if __name__ == '__main__':
    unittest.main()
