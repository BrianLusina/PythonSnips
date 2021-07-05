import unittest
from random import randint

from datastructures.arrays.array_chunks import make_parts


class ArrayChunksTestCase(unittest.TestCase):
    def test_chunks_1(self):
        self.assertListEqual(make_parts([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunks_2(self):
        self.assertListEqual(make_parts([1, 2, 3], 1), [[1], [2], [3]])

    def test_chunks_3(self):
        self.assertListEqual(make_parts([1, 2, 3, 4, 5], 10), [[1, 2, 3, 4, 5]])

    @staticmethod
    def make_parts_solution(arr, chunk_size):
        return [arr[x:x + chunk_size] for x in range(0, len(arr), chunk_size)]

    def test_random_numbers(self):
        for _ in range(10):
            arr = list(range(randint(10, 100)))
            chunk_size = randint(1, 25)
            self.assertListEqual(make_parts(arr, chunk_size), self.make_parts_solution(arr, chunk_size))


if __name__ == '__main__':
    unittest.main()
