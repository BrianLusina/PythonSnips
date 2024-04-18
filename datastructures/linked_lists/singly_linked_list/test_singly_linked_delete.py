import unittest

from . import SinglyLinkedList


class DeleteAtPositionSinglyLInkedListTestCase(unittest.TestCase):
    def test_delete_node_at_position_0(self):
        """should delete a node at position 0 [1,2,3,4,5,6] by 4 to become [2,3,4,5,6]"""
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)

        new_head = linked_list.delete_node_at_position(0)
        expected = [2, 3, 4, 5, 6]

        self.assertIsNotNone(new_head)
        self.assertIsNotNone(new_head.data, 1)
        self.assertEqual(expected, list(linked_list))


if __name__ == "__main__":
    unittest.main()
