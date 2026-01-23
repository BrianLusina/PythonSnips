import unittest
from typing import List
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list.node import SingleNode
from datastructures.linked_lists.linked_list_utils import remove_nth_from_end

REMOVE_NTH_NODE_FROM_END_TEST_CASES = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [0, 1, 2, 3, 4, 5, 7, 8, 9]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, [1, 2, 3, 4, 5, 6, 7, 8, 9])
]


class RemoveNthNodeFromEndTestCase(unittest.TestCase):
    @parameterized.expand(REMOVE_NTH_NODE_FROM_END_TEST_CASES)
    def test_remove_nth_node_from_end(
        self, data: List[int], n: int, expected: List[int]
    ):
        if not data:
            actual = remove_nth_from_end(head=None, n=n)
            self.assertIsNone(actual)

        head = SingleNode(data[0])
        current = head
        for d in data[1:]:
            current.next = SingleNode(d)
            current = current.next

        actual = remove_nth_from_end(head=head, n=n)
        actual_current_head = actual
        actual_data = []
        while actual_current_head:
            actual_data.append(actual_current_head.data)
            actual_current_head = actual_current_head.next

        self.assertListEqual(expected, actual_data)


if __name__ == "__main__":
    unittest.main()
