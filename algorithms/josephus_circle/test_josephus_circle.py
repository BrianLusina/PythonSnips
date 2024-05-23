import unittest
from datastructures.linked_lists.circular import CircularLinkedList
from datastructures.linked_lists.circular.node import CircularNode
from . import josephus_circle


class JosephusCircularTestCase(unittest.TestCase):
    def test_1(self):
        """should run through the circle of 1-2-3-4 with a step of 2 remaining with 1"""
        data = [1, 2, 3, 4]
        circular_linked_list = CircularLinkedList()
        for d in data:
            circular_linked_list.append(d)

        step = 2
        expected = CircularNode(1)
        actual = josephus_circle(circular_linked_list, step)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
