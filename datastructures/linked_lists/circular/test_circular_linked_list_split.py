import unittest
from typing import List, Tuple
from parameterized import parameterized
from datastructures.linked_lists.circular import CircularLinkedList
from datastructures.linked_lists.circular.node import CircularNode


CIRCULAR_LINKED_LIST_SPLIT_LIST_TEST_CASES = [
    ([1, 2, 3, 4, 5, 6], ([1, 2, 3], [4, 5, 6])),
    ([], ([], [])),
    ([1, 5, 7], ([1, 5], [7])),
    ([2, 6, 1, 5], ([2, 6], [1, 5])),
    ([3, 1, 4, 2, 5], ([3, 1, 4], [2, 5])),
    ([8, 10, 12, 14, 16, 18], ([8, 10, 12], [14, 16, 18])),
    ([9, 10], ([9], [10])),
]


class CircularLinkedListSplitListTestCase(unittest.TestCase):
    def assert_data(self, head: CircularNode, expected: List[int]):
        current = head
        actual = []
        while current:
            actual.append(current.data)
            if current.next is head:
                break
            current = current.next

        self.assertListEqual(expected, actual)

    @parameterized.expand(CIRCULAR_LINKED_LIST_SPLIT_LIST_TEST_CASES)
    def test_split_list(self, data: List[int], expected: Tuple[List[int], List[int]]):
        circular_linked_list = CircularLinkedList()
        if not data:
            result = circular_linked_list.split_list()
            self.assertIsNone(result)
            return

        for d in data:
            circular_linked_list.append(d)

        result = circular_linked_list.split_list()
        self.assertIsNotNone(result)

        first_list_head, second_list_head = result
        self.assert_data(first_list_head, expected[0])
        self.assert_data(second_list_head, expected[1])


if __name__ == "__main__":
    unittest.main()
