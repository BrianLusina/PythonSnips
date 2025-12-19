import unittest
from typing import List
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list.single_linked_list import (
    SinglyLinkedList,
)

TEST_CASES = [
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 1, 2, 2, 3, -1, 10, 12], [1, 12, 1, 10, 2, -1, 2, 3]),
    ([10, 20, -22, 21, -12], [10, -12, 20, 21, -22]),
    ([1, 3, 5, 7, 9, 10, 8, 6, 4, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    (
        [7, 0, 10, 13, 12, 19, 1, 3, 6, 7, 4, 2, 11],
        [7, 11, 0, 2, 10, 4, 13, 7, 12, 6, 19, 3, 1],
    ),
    ([0, 8, 3, 1, 2, 7], [0, 7, 8, 2, 3, 1]),
    ([7, 4, 6, 1, 5, 8], [7, 8, 4, 5, 6, 1]),
    ([9, 0, 8, 2], [9, 2, 0, 8]),
    ([6, 8, 7], [6, 7, 8]),
]


class ReorderListTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_reorder_list(self, input_list: List[int], expected_output: List[int]):
        linked_list = SinglyLinkedList()
        for data in input_list:
            linked_list.append(data)

        actual = linked_list.reorder_list()
        self.assertIsNotNone(actual)

        # since the head node is returned, we want the values of the linked list and not just the head node
        # to check that the actual reordering worked
        actual_list: List[int] = []
        curr = actual
        while curr:
            actual_list.append(curr.data)
            curr = curr.next

        self.assertEqual(expected_output, actual_list)


if __name__ == "__main__":
    unittest.main()
