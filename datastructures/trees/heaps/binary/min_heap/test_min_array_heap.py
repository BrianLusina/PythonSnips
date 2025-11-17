import unittest

from .min_array_heap import MinArrayBasedHeap


class MaxArrayBasedHeapTestCaseOne(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MinArrayBasedHeap()

    def test_insertion(self):
        """should insert nodes in the correct position in the heap"""
        self.heap.insert(8)
        self.heap.insert(3)
        self.heap.insert(2)
        self.heap.insert(7)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(4)
        actual = self.heap.root_node
        actual_last_node = self.heap.last_node
        expected_root_node = 1
        expected_last_node = 4
        self.assertEqual(expected_root_node, actual)
        self.assertEqual(expected_last_node, actual_last_node)


if __name__ == "__main__":
    unittest.main()
