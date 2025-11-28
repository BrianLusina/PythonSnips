from typing import List
import unittest
from parameterized import parameterized
from datastructures.linked_lists.singly_linked_list.single_linked_list import (
    SinglyLinkedList,
)


class ReverseBetweenSinglyLinkedListTestCase(unittest.TestCase):
    def test_return_none_for_empty_linked_list(self):
        """should return none for an empty linked list when attempting to reverse"""
        linked_list = SinglyLinkedList()

        actual = linked_list.reverse_between(0, 1)
        self.assertIsNone(actual)

    def test_raises_exception_for_invalid_arguments(self):
        """should raise an exception for invalid left and right arguments"""
        linked_list = SinglyLinkedList()

        with self.assertRaises(ValueError):
            linked_list.reverse_between(10, 9)

    @parameterized.expand(
        [
            ([1, 2, 3, 4, 5, 4, 3, 2, 1], 1, 9, [1, 2, 3, 4, 5, 4, 3, 2, 1]),
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
            (
                [103, 7, 10, -9, 105, 67, 31, 63],
                1,
                8,
                [63, 31, 67, 105, -9, 10, 7, 103],
            ),
            (
                [103, 7, 10, -9, 105, 67, 31, 63],
                1,
                8,
                [63, 31, 67, 105, -9, 10, 7, 103],
            ),
            ([-499, 399, -299, 199, -99, 9], 3, 5, [-499, 399, -99, 199, -299, 9]),
            ([7, -9, 2, -10, 1, -8, 6], 2, 5, [7, 1, -10, 2, -9, -8, 6]),
            ([6, 8, 7], 1, 2, [8, 6, 7]),
            ([9, 0, 8, 2], 2, 4, [9, 2, 8, 0]),
            ([7, 4, 6, 1, 5, 8], 2, 5, [7, 5, 1, 6, 4, 8]),
            ([3, 7, 12, 2, 5, 1], 3, 6, [3, 7, 1, 5, 2, 12]),
            ([3, 6, 7, 4, 2], 2, 4, [3, 4, 7, 6, 2]),
        ]
    )
    def test_reverse_between(
        self, data: List[int], left: int, right: int, expected: List[int]
    ):
        """should reverse linked list between left and right arguments"""
        linked_list = SinglyLinkedList()
        # add the data to the linked list
        for d in data:
            linked_list.append(d)

        # perform reversal
        actual = linked_list.reverse_between(left, right)

        # since the head node is returned, we want the values of the linked list and not just the head node
        # to check that the actual reversal worked
        actual_list: List[int] = []
        curr = actual
        while curr:
            actual_list.append(curr.data)
            curr = curr.next

        # perform assertion
        self.assertEqual(expected, actual_list)

    @parameterized.expand(
        [
            ([1, 2, 3, 4, 5, 4, 3, 2, 1], 1, 9, [1, 2, 3, 4, 5, 4, 3, 2, 1]),
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
            (
                [103, 7, 10, -9, 105, 67, 31, 63],
                1,
                8,
                [63, 31, 67, 105, -9, 10, 7, 103],
            ),
            (
                [103, 7, 10, -9, 105, 67, 31, 63],
                1,
                8,
                [63, 31, 67, 105, -9, 10, 7, 103],
            ),
            ([-499, 399, -299, 199, -99, 9], 3, 5, [-499, 399, -99, 199, -299, 9]),
            ([7, -9, 2, -10, 1, -8, 6], 2, 5, [7, 1, -10, 2, -9, -8, 6]),
            ([6, 8, 7], 1, 2, [8, 6, 7]),
            ([9, 0, 8, 2], 2, 4, [9, 2, 8, 0]),
            ([7, 4, 6, 1, 5, 8], 2, 5, [7, 5, 1, 6, 4, 8]),
            ([3, 7, 12, 2, 5, 1], 3, 6, [3, 7, 1, 5, 2, 12]),
            ([3, 6, 7, 4, 2], 2, 4, [3, 4, 7, 6, 2]),
        ]
    )
    def test_reverse_between_with_dummy(
        self, data: List[int], left: int, right: int, expected: List[int]
    ):
        """should reverse linked list between left and right arguments"""
        linked_list = SinglyLinkedList()
        # add the data to the linked list
        for d in data:
            linked_list.append(d)

        # perform reversal
        actual = linked_list.reverse_between_with_dummy(left, right)

        # since the head node is returned, we want the values of the linked list and not just the head node
        # to check that the actual reversal worked
        actual_list: List[int] = []
        curr = actual
        while curr:
            actual_list.append(curr.data)
            curr = curr.next

        # perform assertion
        self.assertEqual(expected, actual_list)


if __name__ == "__main__":
    unittest.main()
