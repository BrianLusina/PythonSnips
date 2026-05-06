import unittest
from typing import List
from parameterized import parameterized, parameterized_class
from datastructures.sparse_vector import SparseVector

SPARSE_VECTOR_TEST_CASES = [([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8)]


@parameterized_class(("nums1", "nums2", "expected"), SPARSE_VECTOR_TEST_CASES)
class SparseVectorTestCase(unittest.TestCase):
    def test_dot_product(self):
        vector_one = SparseVector(self.nums_1)
        vector_two = SparseVector(self.nums_2)
        actual = vector_one.dot_product(vector_two)

        self.assertEqual(self.expected, actual)


if __name__ == "__main__":
    unittest.main()
