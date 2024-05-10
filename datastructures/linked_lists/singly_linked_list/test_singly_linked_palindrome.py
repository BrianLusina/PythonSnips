import unittest

from . import SinglyLinkedList


class LinkedListIsPalindromeTestCase(unittest.TestCase):
    def test_1(self):
        """should return true for ["r", "a", "c", "e", "c", "a", "r"]"""
        linked_list = SinglyLinkedList()
        data = ["r", "a", "c", "e", "c", "a", "r"]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
