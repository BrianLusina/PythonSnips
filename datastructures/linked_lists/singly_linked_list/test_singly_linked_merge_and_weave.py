from typing import List
import unittest
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list.single_linked_list import (
    SinglyLinkedList,
)
from datastructures.linked_lists.singly_linked_list.single_linked_list_utils import (
    merge_and_weave,
)

TEST_CASES = [
    ([1, 2, 3], [6, 5, 4], [1, 6, 2, 5, 3, 4]),
    ([1, 2, 3], [4, 5], [1, 4, 2, 5, 3]),
]


class MergeAndWeaveSinglyLinkedListTestCase(unittest.TestCase):
    def test_return_none_for_empty_linked_list(self):
        """should return none for an empty linked list when attempting to reverse"""
        linked_list_one = SinglyLinkedList()
        linked_list_two = SinglyLinkedList()

        actual = merge_and_weave(linked_list_one.head, linked_list_two.head)
        self.assertIsNone(actual)

    @parameterized.expand(TEST_CASES)
    def test_merge_and_weave(
        self, list_one_data: List[int], list_two_data: List[int], expected: List[int]
    ):
        linked_list_one = SinglyLinkedList()
        # add the data to the linked list
        for d in list_one_data:
            linked_list_one.append(d)

        linked_list_two = SinglyLinkedList()
        # add the data to the linked list
        for d in list_two_data:
            linked_list_two.append(d)

        actual = merge_and_weave(linked_list_one.head, linked_list_two.head)

        actual_list: List[int] = []
        curr = actual
        while curr:
            actual_list.append(curr.data)
            curr = curr.next

        # perform assertion
        self.assertEqual(expected, actual_list)


if __name__ == "__main__":
    unittest.main()
