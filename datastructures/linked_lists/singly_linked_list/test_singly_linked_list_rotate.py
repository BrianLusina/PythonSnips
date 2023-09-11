import unittest

from . import SinglyLinkedList


class RotateSinglyLInkedListTestCase(unittest.TestCase):
    def test_rotates_non_empty_list_by_4(self):
        """should rotate [1,2,3,4,5,6] by 4 to become [5, 6, 1, 2, 3, 4]"""
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)

        new_head = linked_list.rotate(4)
        expected = [5, 6, 1, 2, 3, 4]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 5)
        self.assertEqual(expected, list(linked_list))

    def test_rotates_non_empty_list_1_2_3_4_5_by_2(self):
        """Rotates [1,2,3,4,5] by 2 to become [4,5,1,2,3]"""
        linked_list = SinglyLinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        new_head = linked_list.rotate(2)
        expected = [4, 5, 1, 2, 3]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 4)
        self.assertEqual(expected, list(linked_list))

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


if __name__ == '__main__':
    unittest.main()
