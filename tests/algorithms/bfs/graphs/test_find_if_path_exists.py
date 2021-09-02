import unittest

from algorithms.bfs.graphs.find_if_path_exists import valid_path


class FindIfPathExistsInGraphTestCases(unittest.TestCase):
    def test_returns_true_for_0_1_1_2_2_0(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        start = 0
        end = 2

        self.assertTrue(valid_path(n, edges, start, end))

    def test_returns_false_for_0_1_1_2_2_0(self):
        n = 6
        edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
        start = 0
        end = 5

        self.assertFalse(valid_path(n, edges, start, end))

    def test_returns_true_for_empty_list(self):
        n = 1
        edges = []
        start = 0
        end = 0

        self.assertTrue(valid_path(n, edges, start, end))


if __name__ == '__main__':
    unittest.main()
