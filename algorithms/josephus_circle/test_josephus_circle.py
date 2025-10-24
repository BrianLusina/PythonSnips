import unittest
from datastructures.linked_lists.circular import CircularLinkedList
from datastructures.linked_lists.circular.node import CircularNode
from . import josephus_circle, josephus_survivor


class JosephusCircleTestCase(unittest.TestCase):
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


class JosephusSurvivorTestCase(unittest.TestCase):
    def test_1(self):
        """should run through the circle of n=7, k=3 to return 4"""
        n = 7
        k = 3
        expected = 4
        actual = josephus_survivor(n, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should run through the circle of n=11, k=19 to return 10"""
        n = 11
        k = 19
        expected = 10
        actual = josephus_survivor(n, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should run through the circle of n=1, k=300 to return 1"""
        n = 1
        k = 300
        expected = 1
        actual = josephus_survivor(n, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should run through the circle of n=14, k=2 to return 13"""
        n = 14
        k = 2
        expected = 13
        actual = josephus_survivor(n, k)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should run through the circle of n=100, k=1 to return 100"""
        n = 100
        k = 1
        expected = 100
        actual = josephus_survivor(n, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
