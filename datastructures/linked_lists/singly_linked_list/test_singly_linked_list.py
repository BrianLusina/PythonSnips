from typing import List, Callable
import unittest

from . import SinglyLinkedList, SingleNode


class SinglyLinkedListTest(unittest.TestCase):
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def test_empty_list_has_len_zero(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(len(linked_list), 0)

    def test_singleton_list_has_len_one(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        self.assertEqual(len(linked_list), 1)

    def test_non_empty_list_has_correct_len(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(len(linked_list), 3)

    def test_singleton_list_has_head(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        self.assertEqual(linked_list.head.data, 1)

    def test_non_empty_list_has_correct_head(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        self.assertEqual(linked_list.head.data, 1)

    def test_can_push_to_non_empty_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        self.assertEqual(len(linked_list), 4)

    def test_pushing_to_empty_list_changes_head(self):
        linked_list = SinglyLinkedList()
        linked_list.append(5)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list.head.data, 5)

    def test_can_from_non_empty_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        self.assertEqual(linked_list.pop().data, 5)
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list.head.data, 3)

    def test_pop_from_singleton_list_removes_head(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        self.assertEqual(linked_list.pop().data, 1)
        self.assertEqual(len(linked_list), 0)
        self.assertIsNone(linked_list.head)

    def test_error_on_empty_list_pop(self):
        linked_list = SinglyLinkedList()
        actual = linked_list.pop()
        self.assertIsNone(actual)

    def test_push_and_pop(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertEqual(len(linked_list), 3)
        self.assertEqual(linked_list.pop().data, 3)
        self.assertEqual(linked_list.pop().data, 2)
        self.assertEqual(linked_list.pop().data, 1)
        self.assertEqual(len(linked_list), 0)
        linked_list.append(4)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list.head.data, 4)

    def test_singleton_list_head_has_no_next(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        self.assertIsNone(linked_list.head.next)

    def test_non_empty_list_traverse(self):
        linked_list = SinglyLinkedList()
        for i in range(10):
            linked_list.append(i)

        current = linked_list.head
        for i in range(10):
            self.assertEqual(current.data, i)
            current = current.next
        self.assertIsNone(current)

    def test_empty_linked_list_to_list_is_empty(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(list(linked_list), [])

    def test_singleton_linked_list_to_list_list_with_singular_element(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        self.assertEqual(list(linked_list), [1])

    def test_non_empty_linked_list_to_list_is_list_with_all_elements(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(list(linked_list), [1, 2, 3])

    def test_reversed_singleton_list_is_same_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        reversed_linked_list = linked_list.reverse()
        self.assertEqual(reversed_linked_list.data, 1)

    def test_reverse_non_empty_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        linked_list.reverse()
        self.assertEqual(list(linked_list), [3, 2, 1])

    def test_rotates_non_empty_list_by_4(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)

        new_head = linked_list.rotate(4)

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 5)
        self.assertEqual(list(linked_list), [5, 6, 1, 2, 3, 4])

    def test_reverse_groups_of_4_of_non_empty_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)

        new_head = linked_list.reverse_groups(4, linked_list.head)

        self.assertIsNotNone(new_head)
        self.assertEqual(4, new_head.data)

    def test_reverse_groups_of_3_of_non_empty_list(self):
        linked_list = SinglyLinkedList()
        linked_list.append(9)
        linked_list.append(8)
        linked_list.append(7)
        linked_list.append(6)
        linked_list.append(5)
        linked_list.append(4)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)

        new_head = linked_list.reverse_groups(3)

        self.assertIsNotNone(new_head)
        self.assertEqual(7, new_head.data)

    def test_reverse_groups_of_0_of_non_empty_list_returns_initial_head(self):
        linked_list = SinglyLinkedList()
        linked_list.append(9)
        linked_list.append(8)
        linked_list.append(7)
        linked_list.append(6)
        linked_list.append(5)
        linked_list.append(4)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)

        new_head = linked_list.reverse_groups(0)

        self.assertIsNotNone(new_head)
        self.assertEqual(9, new_head.data)


class SinglyLinkedListKthToLastNodeTestCases(unittest.TestCase):
    """Kth to Last node test cases"""

    def test_1(self):
        """should return correct nodes for linked list of a->b->c->d"""
        linked_list = SinglyLinkedList()
        linked_list.append("a")
        linked_list.append("b")
        linked_list.append("c")
        linked_list.append("d")

        expected_d = SingleNode("d")
        actual = linked_list.kth_to_last_node(1)
        self.assertEqual(expected_d, actual)

        expected_c = SingleNode("c")
        actual = linked_list.kth_to_last_node(2)
        self.assertEqual(expected_c, actual)

        expected_b = SingleNode("b")
        actual = linked_list.kth_to_last_node(3)
        self.assertEqual(expected_b, actual)

        expected_a = SingleNode("a")
        actual = linked_list.kth_to_last_node(4)
        self.assertEqual(expected_a, actual)


class SinglyLinkedDeleteMiddleNodeTestCases(unittest.TestCase):
    """Delete Middle node test cases"""

    def test_1(self):
        """should return middle node for linked list of [1,3,4,7,1,2,6]"""
        data = [1, 3, 4, 7, 1, 2, 6]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(7)
        actual = linked_list.delete_middle_node()
        self.assertEqual(expected_middle_node, actual)

    def test_2(self):
        """should return middle node for linked list of [1,2,3,4]"""
        data = [1, 2, 3, 4]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(3)
        actual = linked_list.delete_middle_node()
        self.assertEqual(expected_middle_node, actual)

    def test_3(self):
        """should return middle node for linked list of [2,1]"""
        data = [2, 1]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(1)
        actual = linked_list.delete_middle_node()
        self.assertEqual(expected_middle_node, actual)

    def test_1_2_pointers(self):
        """should return middle node for linked list of [1,3,4,7,1,2,6]"""
        data = [1, 3, 4, 7, 1, 2, 6]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(7)
        actual = linked_list.delete_middle_node_2_pointers()
        self.assertEqual(expected_middle_node, actual)

    def test_2_2_pointers(self):
        """should return middle node for linked list of [1,2,3,4]"""
        data = [1, 2, 3, 4]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(3)
        actual = linked_list.delete_middle_node_2_pointers()
        self.assertEqual(expected_middle_node, actual)

    def test_3_2_pointers(self):
        """should return middle node for linked list of [2,1]"""
        data = [2, 1]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        expected_middle_node = SingleNode(1)
        actual = linked_list.delete_middle_node_2_pointers()
        self.assertEqual(expected_middle_node, actual)


class SinglyLinkedOddEvenListTestCases(unittest.TestCase):
    """OddEventList test cases"""

    def run_test(self, data: List[int], expected: List[int]):
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        actual_head = linked_list.odd_even_list()
        actual_nodes = []

        while actual_head:
            actual_nodes.append(actual_head.data)
            actual_head = actual_head.next

        zipped = zip(expected, actual_nodes)

        for (expected, actual_node) in zipped:
            self.assertEqual(expected, actual_node)

    def test_1(self):
        """should return [1,3,5,2,4] for linked list of [1,2,3,4,5]"""
        data = [1, 2, 3, 4, 5]
        expected_list = [1, 3, 5, 2, 4]

        self.run_test(data, expected_list)

    def test_2(self):
        """should return [2,3,6,7,1,5,4] for linked list of [2,1,3,5,6,4,7]"""
        data = [2, 1, 3, 5, 6, 4, 7]
        expected_list = [2, 3, 6, 7, 1, 5, 4]
        self.run_test(data, expected_list)


class SinglyLinkedMaximumPairSumTestCases(unittest.TestCase):
    """Maximum Pair Sum test cases"""

    def test_1_using_list_of_integers(self):
        """should return 6 from a list of [5,4,2,1]"""
        data = [5, 4, 2, 1]
        expected = 6
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum()

        self.assertEqual(expected, actual)

    def test_2_using_list_of_integers(self):
        """should return 7 for linked list of [4,2,2,3]"""
        data = [4, 2, 2, 3]
        expected = 7
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum()

        self.assertEqual(expected, actual)

    def test_3_using_list_of_integers(self):
        """should return 100001 for linked list of [1,100000]"""
        data = [1, 100000]
        expected = 100001
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum()

        self.assertEqual(expected, actual)

    def test_1_using_stack(self):
        """should return 6 from a list of [5,4,2,1]"""
        data = [5, 4, 2, 1]
        expected = 6
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_stack()

        self.assertEqual(expected, actual)

    def test_2_using_stack(self):
        """should return 7 for linked list of [4,2,2,3]"""
        data = [4, 2, 2, 3]
        expected = 7
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_stack()

        self.assertEqual(expected, actual)

    def test_3_using_stack(self):
        """should return 100001 for linked list of [1,100000]"""
        data = [1, 100000]
        expected = 100001
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_stack()

        self.assertEqual(expected, actual)

    def test_1_using_reverse_in_place(self):
        """should return 6 from a list of [5,4,2,1]"""
        data = [5, 4, 2, 1]
        expected = 6
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_reverse_in_place()

        self.assertEqual(expected, actual)

    def test_2_using_reverse_in_place(self):
        """should return 7 for linked list of [4,2,2,3]"""
        data = [4, 2, 2, 3]
        expected = 7
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_reverse_in_place()

        self.assertEqual(expected, actual)

    def test_3_using_reverse_in_place(self):
        """should return 100001 for linked list of [1,100000]"""
        data = [1, 100000]
        expected = 100001
        linked_list = SinglyLinkedList()

        for d in data:
            linked_list.append(d)

        actual = linked_list.maximum_pair_sum_reverse_in_place()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
