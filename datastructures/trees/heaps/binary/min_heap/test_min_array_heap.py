import unittest

from datastructures.trees.heaps.binary.min_heap.min_array_heap import MinArrayBasedHeap


class MaxArrayBasedHeapTestCaseOne(unittest.TestCase):
    def test_insertion(self):
        """should insert nodes in the correct position in the heap"""
        heap = MinArrayBasedHeap()
        heap.insert(8)
        heap.insert(3)
        heap.insert(2)
        heap.insert(7)
        heap.insert(9)
        heap.insert(1)
        heap.insert(4)
        actual = heap.root_node
        actual_last_node = heap.last_node
        expected_root_node = 1
        expected_last_node = 4
        self.assertEqual(expected_root_node, actual)
        self.assertEqual(expected_last_node, actual_last_node)

    def test_insertion_on_empty_data(self):
        """should insert nodes in the correct position in the heap"""
        heap = MinArrayBasedHeap()
        heap.insert(8)
        actual = heap.root_node
        actual_last_node = heap.last_node
        expected_root_node = 8
        expected_last_node = 8
        self.assertEqual(expected_root_node, actual)
        self.assertEqual(expected_last_node, actual_last_node)

    def test_initialized_with_data(self):
        """should insert nodes in the correct position in the heap when given an array of data"""
        initial_data = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        expected_data = [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
        heap = MinArrayBasedHeap(data=initial_data)
        actual = heap.root_node
        actual_last_node = heap.last_node
        expected_root_node = -5
        expected_last_node = 41
        self.assertEqual(expected_root_node, actual)
        self.assertEqual(expected_last_node, actual_last_node)

        # insert 76
        heap.insert(76)
        actual_peak_neg_5 = heap.peak()
        self.assertEqual(-5, actual_peak_neg_5)

        actual_del_neg_5 = heap.delete()
        self.assertEqual(-5, actual_del_neg_5)

        actual_peak_2 = heap.peak()
        self.assertEqual(2, actual_peak_2)


if __name__ == "__main__":
    unittest.main()
