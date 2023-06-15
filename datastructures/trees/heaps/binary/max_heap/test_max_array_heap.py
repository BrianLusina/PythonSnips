import unittest

from .max_array_heap import MaxArrayBasedHeap


class MaxArrayBasedHeapTestCaseOne(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = MaxArrayBasedHeap()

    def test_insertion(self):
        self.heap.insert_data(100)
        actual = self.heap.root_node
        expected = 100
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
