import unittest

from . import DoublyLinkedList


class DoublyLinkedListAppendPrependTests(unittest.TestCase):
    def test_append(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(10)
        doubly_linked_list.append(20)

        self.assertEqual(2, len(doubly_linked_list))

    def test_prepend(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(10)
        doubly_linked_list.append(20)

        self.assertEqual(2, len(doubly_linked_list))

        doubly_linked_list.prepend(30)
        doubly_linked_list.prepend(40)

        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(40, doubly_linked_list.head.data)


class DoublyLinkedListInsertAfterAndBeforeNodeTests(unittest.TestCase):
    def test_insert_e_after_b(self):
        """Should insert E after B in list A-B-C-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("B")
        new_data = "E"

        doubly_linked_list.insert_after_node(key, new_data)
        expected = ["A", "B", new_data, "C", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_insert_e_before_b(self):
        """Should insert E before B in list A-B-C-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("B")
        new_data = "E"

        doubly_linked_list.insert_before_node(key, new_data)
        expected = ["A", new_data, "B", "C", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))


class DoublyLinkedListDeleteNodeTests(unittest.TestCase):
    def test_1(self):
        """Should delete the only node in the list A"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(1, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        doubly_linked_list.delete_node_by_key(hash("A"))

        self.assertEqual(0, len(doubly_linked_list))

    def test_2(self):
        """Should delete the head node in list A-B-C-D to become B-C-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("A")

        doubly_linked_list.delete_node_by_key(key)
        expected = ["B", "C", "D"]

        self.assertEqual(3, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_3(self):
        """Should delete a middle node in list A-B-C-D to become A-B-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("C")

        doubly_linked_list.delete_node_by_key(key)
        expected = ["A", "B", "D"]

        self.assertEqual(3, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_4(self):
        """Should delete tail node in list A-B-C-D to become A-B-C"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(4, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("D")

        doubly_linked_list.delete_node_by_key(key)
        expected = ["A", "B", "C"]

        self.assertEqual(3, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_1_2(self):
        """Should delete the only node in the list A"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(1, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        doubly_linked_list.delete_nodes_by_key(hash("A"))

        self.assertEqual(0, len(doubly_linked_list))

    def test_2_1(self):
        """Should delete the head node in list A-B-B-C-D-D to become B-B-C-D-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "B", "C", "D", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(6, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("A")

        doubly_linked_list.delete_nodes_by_key(key)
        expected = ["B", "B", "C", "D", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_3_1(self):
        """Should delete a middle nodes in list A-A-B-B-B-C-D-D to become A-A-C-D-D"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "A", "B", "B", "B", "C", "D", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(8, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("B")

        doubly_linked_list.delete_nodes_by_key(key)
        expected = ["A", "A", "C", "D", "D"]

        self.assertEqual(5, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_4_1(self):
        """Should delete tail node in list A-B-C-D-D-D to become A-B-C"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D", "D", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(6, len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        key = hash("D")

        doubly_linked_list.delete_nodes_by_key(key)
        expected = ["A", "B", "C"]

        self.assertEqual(3, len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))


class DoublyLinkedListReverseTests(unittest.TestCase):
    def test_1(self):
        """Should reverse list of A<>B<>C<>D to D<>C<>B<>A"""
        doubly_linked_list = DoublyLinkedList()

        data = ["A", "B", "C", "D"]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(len(data), len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        expected = list(reversed(data))

        actual = doubly_linked_list.reverse()
        self.assertEqual(expected[0], actual.data)

        self.assertEqual(len(expected), len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))


class DoublyLinkedListRemoveDuplicatesTests(unittest.TestCase):
    def test_1(self):
        """Should remove duplicates from list of 1<>4<>7<>4 to 1<>4<>7"""
        doubly_linked_list = DoublyLinkedList()

        data = [1, 4, 7, 4]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(len(data), len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        expected = list(set(data))

        doubly_linked_list.remove_duplicates()

        self.assertEqual(len(expected), len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_2(self):
        """Should remove duplicates from list of 8-4-4-6-4-8-4-10-12-12 to 8-4-6-10-12"""
        doubly_linked_list = DoublyLinkedList()

        data = [8, 4, 4, 6, 4, 8, 4, 10, 12, 12]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(len(data), len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        expected = [8, 4, 6, 10, 12]

        doubly_linked_list.remove_duplicates()

        self.assertEqual(len(expected), len(doubly_linked_list))
        self.assertEqual(expected, list(doubly_linked_list))

    def test_3(self):
        """Should do nothing for an empty list i.e. no head"""
        doubly_linked_list = DoublyLinkedList()

        doubly_linked_list.remove_duplicates()

        self.assertEqual(0, len(doubly_linked_list))
        self.assertEqual([], list(doubly_linked_list))

    def test_4(self):
        """Should do nothing for a list with one node"""
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.append(1)

        doubly_linked_list.remove_duplicates()

        self.assertEqual(1, len(doubly_linked_list))
        self.assertEqual([1], list(doubly_linked_list))


class DoublyLinkedListPairsWithSumTests(unittest.TestCase):
    def test_1(self):
        """Should return [(1, 4), (2, 3)] with a target of 5 from list of [1,2,3,4,5]"""
        doubly_linked_list = DoublyLinkedList()

        data = [1, 2, 3, 4, 5]
        for d in data:
            doubly_linked_list.append(d)

        # validate that the append operation is still okay
        self.assertEqual(len(data), len(doubly_linked_list))
        self.assertEqual(data, list(doubly_linked_list))

        expected = [(1, 4), (2, 3)]
        target = 5

        actual = doubly_linked_list.pairs_with_sum(target)
        actual_data = []
        for n1, n2 in actual:
            actual_data.append((n1.data, n2.data))

        self.assertEqual(len(expected), len(actual))
        self.assertEqual(expected, actual_data)


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def test_push_pop(self):
        self.list.append(10)
        self.list.append(20)

        self.assertEqual(2, len(self.list))

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(1, len(self.list))

        self.assertEqual(10, self.list.pop().data)
        self.assertEqual(0, len(self.list))

    def test_push_shift(self):
        self.list.append(10)
        self.list.append(20)

        self.assertEqual(2, len(self.list))

        self.assertEqual(10, self.list.shift())
        self.assertEqual(1, len(self.list))

        self.assertEqual(20, self.list.shift())
        self.assertEqual(0, len(self.list))

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(2, len(self.list))

        self.assertEqual(20, self.list.shift())
        self.assertEqual(1, len(self.list))

        self.assertEqual(10, self.list.shift())
        self.assertEqual(0, len(self.list))

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(2, len(self.list))

        self.assertEqual(10, self.list.pop().data)
        self.assertEqual(1, len(self.list))

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(0, len(self.list))

    def test_all(self):
        # list is []
        self.assertEqual(0, len(self.list))

        self.list.append(10)
        self.assertEqual(1, len(self.list))
        # list is 10->None

        self.list.append(20)
        self.assertEqual(2, len(self.list))
        # list is 10<->20->None

        self.assertEqual(20, self.list.pop().data)
        self.assertEqual(1, len(self.list))
        # list is 10<->None

        self.list.append(30)
        self.assertEqual(2, len(self.list))
        # list is 10<->30->None

        self.assertEqual(10, self.list.shift())
        self.assertEqual(1, len(self.list))
        # list is 30->None

        self.list.unshift(40)
        self.assertEqual(2, len(self.list))
        # list is 40<->30->None

        self.list.append(50)
        self.assertEqual(3, len(self.list))
        # list is 40<->30<->50->None

        self.assertEqual(40, self.list.shift())
        self.assertEqual(2, len(self.list))
        # list is 30<->50->None

        self.assertEqual(50, self.list.pop().data)
        self.assertEqual(1, len(self.list))
        # list is 30->None

        self.assertEqual(30, self.list.shift())
        self.assertEqual(0, len(self.list))
        # list is []


if __name__ == "__main__":
    unittest.main()
