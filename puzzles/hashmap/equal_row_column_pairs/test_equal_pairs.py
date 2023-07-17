import unittest
from . import equal_pairs_hash_map, equal_pairs_brute_force, equal_pairs_trie


class EqualPairsTestCase(unittest.TestCase):
    def test_one(self):
        """should return 1 from [[3,2,1],[1,7,6],[2,7,7]]"""
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        expected = 1
        actual = equal_pairs_hash_map(grid)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 3 from [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]"""
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expected = 3
        actual = equal_pairs_hash_map(grid)
        self.assertEqual(expected, actual)


class EqualPairsBruteForceTestCase(unittest.TestCase):
    def test_one(self):
        """should return 1 from [[3,2,1],[1,7,6],[2,7,7]]"""
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        expected = 1
        actual = equal_pairs_brute_force(grid)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 3 from [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]"""
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expected = 3
        actual = equal_pairs_brute_force(grid)
        self.assertEqual(expected, actual)


class EqualPairsTrieTestCase(unittest.TestCase):
    def test_one(self):
        """should return 1 from [[3,2,1],[1,7,6],[2,7,7]]"""
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        expected = 1
        actual = equal_pairs_trie(grid)
        self.assertEqual(expected, actual)

    def test_two(self):
        """should return 3 from [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]"""
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expected = 3
        actual = equal_pairs_trie(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
