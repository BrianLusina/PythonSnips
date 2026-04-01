import unittest
from typing import List
from parameterized import parameterized

from algorithms.counting.rank_teams_by_votes import (
    rank_teams_using_hash_map,
    rank_teams_counting,
)

RANK_TEAMS_BY_VOTES_TEST_CASES = [
    (["ABC", "ACB", "ABC", "ACB", "ACB"], "ACB"),
    (["WXYZ", "XYZW"], "XWYZ"),
    (["ZMNAGUEDSJYLBOPHRQICWFXTVK"], "ZMNAGUEDSJYLBOPHRQICWFXTVK"),
]


class RankTeamsTestCase(unittest.TestCase):
    @parameterized.expand(RANK_TEAMS_BY_VOTES_TEST_CASES)
    def test_rank_teams_hash_map(self, votes: List[str], expected: str):
        actual = rank_teams_using_hash_map(votes)
        self.assertEqual(expected, actual)

    @parameterized.expand(RANK_TEAMS_BY_VOTES_TEST_CASES)
    def test_rank_teams_counting(self, votes: List[str], expected: str):
        actual = rank_teams_counting(votes)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
