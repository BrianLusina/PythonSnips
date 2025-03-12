import unittest

import pytest

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

    def test_2(self):
        """should return true for [2, 4, 6, 4, 2]"""
        linked_list = SinglyLinkedList()
        data = [2, 4, 6, 4, 2]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)

    def test_3(self):
        """should return true for [0, 3, 5, 5, 0]"""
        linked_list = SinglyLinkedList()
        data = [0, 3, 5, 5, 0]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertFalse(actual)

    def test_4(self):
        """should return true for [9, 7, 4, 4, 7, 9]"""
        linked_list = SinglyLinkedList()
        data = [9, 7, 4, 4, 7, 9]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)

    def test_5(self):
        """should return true for [1,2,3,2,1]"""
        linked_list = SinglyLinkedList()
        data = [1,2,3,2,1]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)

    def test_6(self):
        """should return true for [4,7,9,5,4]"""
        linked_list = SinglyLinkedList()
        data = [4,7,9,5,4]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertFalse(actual)

    def test_7(self):
        """should return true for [2,3,5,5,3,2]"""
        linked_list = SinglyLinkedList()
        data = [2,3,5,5,3,2]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)

    def test_8(self):
        """should return true for [6,1,0,5,1,6]"""
        linked_list = SinglyLinkedList()
        data = [6,1,0,5,1,6]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertFalse(actual)


    def test_9(self):
        """should return true for [3,6,9,8,4,8,9,6,3]"""
        linked_list = SinglyLinkedList()
        data = [3,6,9,8,4,8,9,6,3]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome()
        self.assertTrue(actual)

class LinkedListIsPalindromeV2TestCase(unittest.TestCase):
    """
    Tests to check if a linked list is a palindrome using fast and slow pointers approach
    """
    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_1(self):
        """should return true for ["r", "a", "c", "e", "c", "a", "r"]"""
        linked_list = SinglyLinkedList()
        data = ["r", "a", "c", "e", "c", "a", "r"]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_2(self):
        """should return true for [2, 4, 6, 4, 2]"""
        linked_list = SinglyLinkedList()
        data = [2, 4, 6, 4, 2]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_3(self):
        """should return true for [0, 3, 5, 5, 0]"""
        linked_list = SinglyLinkedList()
        data = [0, 3, 5, 5, 0]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertFalse(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_4(self):
        """should return true for [9, 7, 4, 4, 7, 9]"""
        linked_list = SinglyLinkedList()
        data = [9, 7, 4, 4, 7, 9]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_5(self):
        """should return true for [1,2,3,2,1]"""
        linked_list = SinglyLinkedList()
        data = [1,2,3,2,1]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_6(self):
        """should return true for [4,7,9,5,4]"""
        linked_list = SinglyLinkedList()
        data = [4,7,9,5,4]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertFalse(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_7(self):
        """should return true for [2,3,5,5,3,2]"""
        linked_list = SinglyLinkedList()
        data = [2,3,5,5,3,2]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_8(self):
        """should return false for [6,1,0,5,1,6]"""
        linked_list = SinglyLinkedList()
        data = [6,1,0,5,1,6]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertFalse(actual)

    @pytest.mark.linked_list_is_palindrome_fast_and_slow_pointer
    def test_9(self):
        """should return true for [3,6,9,8,4,8,9,6,3]"""
        linked_list = SinglyLinkedList()
        data = [3,6,9,8,4,8,9,6,3]
        for d in data:
            linked_list.append(d)

        actual = linked_list.is_palindrome_2()
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
