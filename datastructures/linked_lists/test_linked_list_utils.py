import unittest
from typing import List
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list.node import SingleNode
from datastructures.linked_lists.linked_list_utils import (
    remove_nth_from_end,
    sum_of_linked_lists,
)

REMOVE_NTH_NODE_FROM_END_TEST_CASES = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [0, 1, 2, 3, 4, 5, 7, 8, 9]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
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


SUM_LINKED_LISTS_TEST_CASES = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]


class SumLinkedListsTestCase(unittest.TestCase):
    @staticmethod
    def construct_linked_list(data: List[int]) -> SingleNode:
        head = SingleNode(data[0])
        current = head
        for d in data[1:]:
            current.next = SingleNode(d)
            current = current.next
        return head

    def assert_data(self, actual: SingleNode, expected: List[int]):
        actual_current_head = actual
        actual_data = []
        while actual_current_head:
            actual_data.append(actual_current_head.data)
            actual_current_head = actual_current_head.next

        self.assertListEqual(expected, actual_data)

    @parameterized.expand(SUM_LINKED_LISTS_TEST_CASES)
    def test_sum_linked_lists(
        self, data_one: List[int], data_two: List[int], expected: List[int]
    ):
        if not data_one and not data_two:
            actual = sum_of_linked_lists(head_one=None, head_two=None)
            self.assertIsNone(actual)

        if not data_one and data_two:
            head = self.construct_linked_list(data_two)
            actual = sum_of_linked_lists(head_one=None, head_two=head)
            self.assertEqual(expected, actual)

        if data_one and not data_two:
            head = self.construct_linked_list(data_one)
            actual = sum_of_linked_lists(head_one=None, head_two=head)
            self.assertEqual(expected, actual)

        head_one = self.construct_linked_list(data_one)
        head_two = self.construct_linked_list(data_two)

        actual = sum_of_linked_lists(head_one=head_one, head_two=head_two)
        self.assertIsNotNone(actual)
        self.assert_data(actual, expected)


if __name__ == "__main__":
    unittest.main()
