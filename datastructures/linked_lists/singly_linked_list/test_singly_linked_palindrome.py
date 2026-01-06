import unittest
from typing import List, Any
from parameterized import parameterized
import pytest

from datastructures.linked_lists.singly_linked_list import SinglyLinkedList

IS_LINKED_LIST_PALINDROME_TEST_CASES = [
    (["r", "a", "c", "e", "c", "a", "r"], True),
    ([2, 4, 6, 4, 2], True),
    ([0, 3, 5, 5, 0], False),
    ([9, 7, 4, 4, 7, 9], True),
    ([1, 2, 3, 2, 1], True),
    ([4, 7, 9, 5, 4], False),
    ([2, 3, 5, 5, 3, 2], True),
    ([6, 1, 0, 5, 1, 6], False),
    ([3, 6, 9, 8, 4, 8, 9, 6, 3], True),
    ([1, 2], False),
    ([1, 2, 3, 4, 5], False),
]


class LinkedListIsPalindromeTestCase(unittest.TestCase):
    @parameterized.expand(IS_LINKED_LIST_PALINDROME_TEST_CASES)
    def test_is_palindrome_using_stack(self, data: List[Any], expected: bool):
        """Tests to check if a linked list is a palindrome using a stack approach"""
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertEqual(expected, actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    @parameterized.expand(IS_LINKED_LIST_PALINDROME_TEST_CASES)
    def test_is_palindrome_using_two_pointers(self, data: List[Any], expected: bool):
        """Tests to check if a linked list is a palindrome using fast and slow pointers approach"""
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
