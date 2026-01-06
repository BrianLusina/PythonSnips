import unittest
from datastructures.linked_lists.singly_linked_list import SingleNode
from datastructures.linked_lists.reorder_list import reorder_list


class ReorderListTestCase(unittest.TestCase):
    def test_1_2_3_4_returns_1_4_2_3(self):
        """Should return 1 -> 4 -> 2 -> 3 from 1 -> 2 -> 3 -> 4"""
        head = SingleNode(
            1, next_=SingleNode(2, next_=SingleNode(3, next_=SingleNode(4)))
        )
        expected_head = SingleNode(
            1, next_=SingleNode(4, next_=SingleNode(2, next_=SingleNode(3)))
        )
        expected = [1, 4, 2, 3]
        reorder_list(head)

        actual = []
        current = head
        while current:
            actual.append(current.data)
            current = current.next

        self.assertEqual(expected_head, head)
        self.assertEqual(expected, actual)

    def test_1_2_3_4_5_returns_1_5_2_4_3(self):
        """Should return 1 -> 5 -> 2 -> 4 -> 3 from 1 -> 2 -> 3 -> 4 -> 5"""
        head = SingleNode(
            1,
            next_=SingleNode(
                2, next_=SingleNode(3, next_=SingleNode(4, next_=SingleNode(5)))
            ),
        )
        expected_head = SingleNode(
            1,
            next_=SingleNode(
                5, next_=SingleNode(2, next_=SingleNode(4, next_=SingleNode(3)))
            ),
        )
        expected = [1, 5, 2, 4, 3]

        reorder_list(head)

        actual = []
        current = head
        while current:
            actual.append(current.data)
            current = current.next

        self.assertEqual(expected_head, head)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
