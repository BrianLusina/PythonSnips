import unittest

from .max_array_heap import MaxArrayBasedHeap


class MaxArrayBasedHeapTestCaseOne(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MaxArrayBasedHeap()

    def test_insertion(self):
        """should insert nodes in the correct position in the heap"""
        self.heap.insert_data(8)
        self.heap.insert_data(3)
        self.heap.insert_data(2)
        self.heap.insert_data(7)
        self.heap.insert_data(9)
        self.heap.insert_data(1)
        self.heap.insert_data(4)
        actual = self.heap.root_node
        actual_last_node = self.heap.last_node
        expected = 9
        expected_last_node = 2
        self.assertEqual(expected, actual)
        self.assertEqual(expected_last_node, actual_last_node)


if __name__ == "__main__":
    unittest.main()
