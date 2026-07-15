import unittest
from typing import Tuple, List
from parameterized import parameterized
from datastructures.map_sum import MapSumBruteForce, MapSumPrefix, MapSumTrie


MAP_SUM_TEST_CASES = [
    (
        [
            ("insert", ("apple", 3)),
            ("sum", ("ap", 3)),
            ("insert", ("apple", 2)),
            ("sum", ("ap", 2)),
        ],
    ),
    (
        [
            ("insert", ("apple", 3)),
            ("sum", ("ap", 3)),
            ("insert", ("ap", 2)),
            ("sum", ("ap", 5)),
        ],
    ),
    (
        [
            ("insert", ("apple", 3)),
            ("insert", ("apple", 5)),
            ("sum", ("ap", 5)),
            ("insert", ("apricot", 2)),
            ("sum", ("ap", 7)),
        ],
    ),
    (
        [
            ("insert", ("car", 3)),
            ("insert", ("cat", 2)),
            ("insert", ("cart", 4)),
            ("sum", ("ca", 9)),
            ("sum", ("car", 7)),
        ],
    ),
    (
        [
            ("insert", ("dog", 5)),
            ("insert", ("cat", 7)),
            ("sum", ("z", 0)),
        ],
    ),
    (
        [
            ("insert", ("a", 3)),
            ("insert", ("apple", 2)),
            ("sum", ("a", 5)),
            ("sum", ("app", 2)),
        ],
    ),
]


class MapSumPairsTestCase(unittest.TestCase):
    @parameterized.expand(MAP_SUM_TEST_CASES)
    def test_map_sum_pairs_brute_force(
        self, operations: List[Tuple[str, Tuple[str, int]]]
    ):
        map_sum = MapSumBruteForce()
        for operation in operations:
            cmd = operation[0]
            params = operation[1]
            if cmd == "insert":
                key, value = params
                map_sum.insert(key, value)

            if cmd == "sum":
                prefix, expected = params
                actual = map_sum.sum(prefix)
                self.assertEqual(expected, actual)

    @parameterized.expand(MAP_SUM_TEST_CASES)
    def test_map_sum_pairs_prefix(self, operations: List[Tuple[str, Tuple[str, int]]]):
        map_sum = MapSumPrefix()
        for operation in operations:
            cmd = operation[0]
            params = operation[1]
            if cmd == "insert":
                key, value = params
                map_sum.insert(key, value)

            if cmd == "sum":
                prefix, expected = params
                actual = map_sum.sum(prefix)
                self.assertEqual(expected, actual)

    @parameterized.expand(MAP_SUM_TEST_CASES)
    def test_map_sum_pairs_trie(self, operations: List[Tuple[str, Tuple[str, int]]]):
        map_sum = MapSumTrie()
        for operation in operations:
            cmd = operation[0]
            params = operation[1]
            if cmd == "insert":
                key, value = params
                map_sum.insert(key, value)

            if cmd == "sum":
                prefix, expected = params
                actual = map_sum.sum(prefix)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
