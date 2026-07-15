import unittest

from . import SinglyLinkedList, SingleNode


class SinglyLinkedListPairwiseTest(unittest.TestCase):
    def test_empty_list(self):
        linked_list = SinglyLinkedList()
        head = linked_list.pairwise_swap()
        self.assertIsNone(head)

    def test_two(self):
        """1 -> 2 -> 3 -> 4 should become 2 -> 1 -> 4 -> 3"""
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.pairwise_swap()

        expected_head = SingleNode(
            2, next_=SingleNode(1, next_=SingleNode(4, next_=SingleNode(3)))
        )

        self.assertEqual(expected_head, actual)

    def test_three(self):
        """7 -> 2 -> 1 should become 2 -> 7 -> 1"""
        linked_list = SinglyLinkedList()
        linked_list.append(7)
        linked_list.append(2)
        linked_list.append(1)

        actual = linked_list.pairwise_swap()

        expected_head = SingleNode(2, next_=SingleNode(7, next_=SingleNode(1)))

        self.assertEqual(expected_head, actual)


if __name__ == "__main__":
    unittest.main()
