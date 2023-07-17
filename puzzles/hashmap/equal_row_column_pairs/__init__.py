from typing import List
from collections import Counter


def equal_pairs_hash_map(grid: List[List[int]]) -> int:
    count = 0
    n = len(grid)

    # keep track of frequency of each row
    row_counter = Counter(tuple(row) for row in grid)

    # add up the frequency of each column in map
    for column in range(n):
        col = [grid[i][column] for i in range(n)]
        count += row_counter[tuple(col)]

    return count


def equal_pairs_brute_force(grid: List[List[int]]) -> int:
    count = 0
    n = len(grid)

    # iterate each row r against each column c
    for r in range(n):
        for c in range(n):
            match = True

            # iterate over row r and column c
            for i in range(n):
                if grid[r][i] != grid[i][c]:
                    match = False
                    break
            count += int(match)
    return count


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, data: List[int]):
        trie = self.trie
        for datum in data:
            if datum not in trie.children:
                trie.children[datum] = TrieNode()
            trie = trie.children[datum]
        trie.count += 1

    def search(self, data: List[int]):
        trie = self.trie
        for d in data:
            if d in trie.children:
                trie = trie.children[d]
            else:
                return 0
        return trie.count


def equal_pairs_trie(grid: List[List[int]]) -> int:
    trie = Trie()
    count = 0
    n = len(grid)

    for row in grid:
        trie.insert(row)

    for c in range(n):
        col_list = [grid[i][c] for i in range(n)]
        count += trie.search(col_list)
    return count
