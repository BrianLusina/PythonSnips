from typing import List
import unittest
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list import SinglyLinkedList
from datastructures.linked_lists.singly_linked_list.single_linked_list_utils import (
    reverse_k_groups,
)

REVERSE_K_GROUP = [
    ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, [7, 8, 9, 4, 5, 6, 1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, [9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
    ([8, 11, 4, 12, 0], 1, [8, 11, 4, 12, 0]),
    ([3, 4, 5, 6, 2, 8, 7, 7], 3, [5, 4, 3, 8, 2, 6, 7, 7]),
    ([1, 2, 3, 4, 5, 6, 7], 7, [7, 6, 5, 4, 3, 2, 1]),
]


class SingleLinkedListReverseKGroupsTestCases(unittest.TestCase):
    @parameterized.expand(REVERSE_K_GROUP)
    def test_reverse_k_groups(self, data: List[int], k: int, expected: List[int]):
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        new_head = linked_list.reverse_groups(k)
        current = new_head
        actual = []
        while current:
            actual.append(current.data)
            current = current.next

        self.assertListEqual(expected, actual)

    @parameterized.expand(REVERSE_K_GROUP)
    def test_reverse_k_groups_utils(self, data: List[int], k: int, expected: List[int]):
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        new_head = reverse_k_groups(linked_list.head, k)
        current = new_head
        actual = []
        while current:
            actual.append(current.data)
            current = current.next

        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
