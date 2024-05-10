import unittest

from . import SinglyLinkedList


class NtToLastNodeSinglyLInkedListTestCase(unittest.TestCase):
    def test_raises_exception_for_negative_value(self):
        """should raise an exception for negative value"""
        linked_list = SinglyLinkedList()

        with self.assertRaises(ValueError):
            linked_list.get_kth_to_last_node(-1)

    def test_raises_exception_for_empty_list(self):
        """should raise an exception for empty list"""
        linked_list = SinglyLinkedList()

        with self.assertRaises(IndexError):
            linked_list.get_kth_to_last_node(1)

    def test_returns_c_for_non_empty_list_a_b_c_d_with_n_2(self):
        """should return C for non-empty list of ["A","B","C","D"] with n = 2"""
        data = ["A", "B", "C", "D"]
        linked_list = SinglyLinkedList()
        for d in data:
            linked_list.append(d)

        actual = linked_list.get_kth_to_last_node(2)
        expected = "C"

        self.assertIsNotNone(actual)
        self.assertEqual(actual.data, expected)

    def test_rotates_non_empty_list_2_0_1_by_4(self):
        """Rotates [0,1,2] by 4 to become [2,0,1]"""
        linked_list = SinglyLinkedList()
        linked_list.append(0)
        linked_list.append(1)
        linked_list.append(2)

        new_head = linked_list.rotate(4)
        expected = [2, 0, 1]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 4)
        self.assertEqual(expected, list(linked_list))


if __name__ == "__main__":
    unittest.main()
