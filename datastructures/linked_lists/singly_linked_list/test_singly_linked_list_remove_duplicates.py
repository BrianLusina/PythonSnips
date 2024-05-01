import unittest

from . import SinglyLinkedList


class RemoveDuplicatesSinglyLinkedListTestCase(unittest.TestCase):
    def test_remove_duplicates_empty_list(self):
        """should return None for empty list"""
        linked_list = SinglyLinkedList()
        actual = linked_list.remove_duplicates()

        self.assertIsNone(actual)

    def test_remove_duplicates_non_empty_list_1(self):
        """Removes duplicates from [1,6,1,4,2,2,4] to become [1,6,4,2]"""
        linked_list = SinglyLinkedList()

        data = [1, 6, 1, 4, 2, 2, 4]
        for d in data:
            linked_list.append(d)

        new_head = linked_list.remove_duplicates()
        expected = [1, 6, 4, 2]

        self.assertIsNotNone(new_head)
        self.assertEqual(expected, list(linked_list))


if __name__ == "__main__":
    unittest.main()
