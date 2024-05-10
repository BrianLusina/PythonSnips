import unittest

from . import DoublyLinkedList


class DoublyLinkedListIsPalindromTests(unittest.TestCase):
    def test_1(self):
        """should return true for ["r", "a", "c", "e", "c", "a", "r"]"""
        linked_list = DoublyLinkedList()
        data = ["r", "a", "c", "e", "c", "a", "r"]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
