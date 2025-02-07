import unittest
from . import SinglyLinkedList


class RemoveNthLastNodeTestCases(unittest.TestCase):

    def test_0(self):
        """should raise ValueError when the value of n is out of bounds"""
        linked_list = SinglyLinkedList()
        data = [43, 68, 11, 5, 69, 37, 70]
        for d in data:
            linked_list.append(d)

        with self.assertRaises(ValueError):
            linked_list.delete_nth_last_node(0)

        with self.assertRaises(ValueError):
            linked_list.delete_nth_last_node(8)

    def test_1(self):
        """should delete nth last node where n=1 and list is 43 -> 68 -> 11 -> 5 -> 69 -> 37 -> 70 to become 43 -> 68 -> 11 -> 5 -> 69 -> 37"""
        linked_list = SinglyLinkedList()
        data = [43, 68, 11, 5, 69, 37, 70]
        for d in data:
            linked_list.append(d)

        new_head = linked_list.delete_nth_last_node(1)
        expected = [43, 68, 11, 5, 69, 37]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 43)
        self.assertEqual(expected, list(linked_list))

    def test_2(self):
        """should delete nth last node where n=3 and list is 23 -> 28 -> 10 -> 5 -> 67 -> 39 -> 70 to become 23 -> 28 -> 10 -> 5 -> 39 -> 70"""
        linked_list = SinglyLinkedList()
        data = [23, 28, 10, 5, 67, 39, 70]
        for d in data:
            linked_list.append(d)

        new_head = linked_list.delete_nth_last_node(3)
        expected = [23, 28, 10, 5, 39, 70]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 23)
        self.assertEqual(expected, list(linked_list))

    def test_3(self):
        """should delete nth last node where n=5 and list is 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 to become 1 -> 2 -> 4 -> 5 -> 6 -> 7"""
        linked_list = SinglyLinkedList()
        data = [1, 2, 3, 4, 5, 6, 7]
        for d in data:
            linked_list.append(d)

        new_head = linked_list.delete_nth_last_node(5)
        expected = [1, 2, 4, 5, 6, 7]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 1)
        self.assertEqual(expected, list(linked_list))

    def test_4(self):
        """should delete nth last node where n=4 and list is 50 -> 40 -> 30 -> 20 to become 40 -> 30 -> 20"""
        linked_list = SinglyLinkedList()
        data = [50, 40, 30, 20]
        for d in data:
            linked_list.append(d)

        new_head = linked_list.delete_nth_last_node(4)
        expected = [40, 30, 20]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 40)
        self.assertEqual(expected, list(linked_list))

    def test_5(self):
        """should delete nth last node where n=6 and list is [69,8,49,106,116,112] to become [8,49,106,116,112]"""
        linked_list = SinglyLinkedList()
        data = [69,8,49,106,116,112]
        for d in data:
            linked_list.append(d)

        n = 6
        new_head = linked_list.delete_nth_last_node(n)
        expected = [8,49,106,116,112]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 8)
        self.assertEqual(expected, list(linked_list))

    def test_6(self):
        """should delete nth last node where n=1 and list is 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 to become 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8"""
        linked_list = SinglyLinkedList()
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for d in data:
            linked_list.append(d)

        n = 1
        new_head = linked_list.delete_nth_last_node(n)
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 1)
        self.assertEqual(expected, list(linked_list))

    def test_7(self):
        """should delete nth last node where n=4 and list is [288,224,275,390,4,383,330,60,193] to become [288,224,275,390,4,330,60,193]"""
        linked_list = SinglyLinkedList()
        data = [288,224,275,390,4,383,330,60,193]
        for d in data:
            linked_list.append(d)

        n = 4
        new_head = linked_list.delete_nth_last_node(n)
        expected = [288,224,275,390,4,330,60,193]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 288)
        self.assertEqual(expected, list(linked_list))

    def test_8(self):
        """should delete nth last node where n=3 and list is [34,53,6,95,38,28,17,63,16,76] to become [34,53,6,95,38,28,17,16,76]"""
        linked_list = SinglyLinkedList()
        data = [34,53,6,95,38,28,17,63,16,76]
        for d in data:
            linked_list.append(d)

        n = 3
        new_head = linked_list.delete_nth_last_node(n)
        expected = [34,53,6,95,38,28,17,16,76]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 34)
        self.assertEqual(expected, list(linked_list))

    def test_9(self):
        """should delete nth last node where n=2 and list is [23,28,10,5,67,39,70,28] to become [23,28,10,5,67,39,28]"""
        linked_list = SinglyLinkedList()
        data = [23,28,10,5,67,39,70,28]
        for d in data:
            linked_list.append(d)

        n = 2
        new_head = linked_list.delete_nth_last_node(n)
        expected = [23,28,10,5,67,39,28]

        self.assertIsNotNone(new_head)
        self.assertEqual(new_head.data, 23)
        self.assertEqual(expected, list(linked_list))


if __name__ == '__main__':
    unittest.main()
