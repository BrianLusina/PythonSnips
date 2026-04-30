import unittest
from typing import List
from parameterized import parameterized
from algorithms.union_find.acounts_merge import accounts_merge
from utils.test_utils import custom_test_name_func

ACCOUNTS_MERGE_TEST_CASES = [
    (
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
    ),
    (
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ],
        [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ],
    ),
    (
        [
            ["Emma", "emma@mail.com", "emma_work@mail.com"],
            ["Bob", "bob_home@mail.com", "bob123@mail.com"],
            ["Emma", "emma_art@mail.com", "emma_work@mail.com"],
            ["Bob", "bob321@mail.com"],
        ],
        [
            ["Emma", "emma@mail.com", "emma_art@mail.com", "emma_work@mail.com"],
            ["Bob", "bob123@mail.com", "bob_home@mail.com"],
            ["Bob", "bob321@mail.com"],
        ],
    ),
    (
        [
            ["Sarah", "sarah@mail.com", "sh@mail.com"],
            ["Sarah", "sarah1@mail.com", "sarahh@mail.com"],
            ["Sarah", "sh3@mail.com"],
        ],
        [
            ["Sarah", "sarah@mail.com", "sh@mail.com"],
            ["Sarah", "sarah1@mail.com", "sarahh@mail.com"],
            ["Sarah", "sh3@mail.com"],
        ],
    ),
    (
        [
            ["Alice", "alice@mail.com"],
            ["Alice", "alice_alice@mail.com", "alice@mail.com"],
            ["Alice", "alice@mail.com", "alice123@mail.com", "aalicee@mail.com"],
        ],
        [
            [
                "Alice",
                "aalicee@mail.com",
                "alice123@mail.com",
                "alice@mail.com",
                "alice_alice@mail.com",
            ]
        ],
    ),
]


class AccountsMergeTestCase(unittest.TestCase):
    @parameterized.expand(ACCOUNTS_MERGE_TEST_CASES, name_func=custom_test_name_func)
    def test_accounts_merge(self, accounts: List[List[str]], expected: List[List[str]]):
        actual = accounts_merge(accounts)
        self.assertEqual(sorted(expected), sorted(actual))


if __name__ == "__main__":
    unittest.main()
