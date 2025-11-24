from typing import List
from datastructures import DisjointSetUnion, UnionFind


def num_similar_groups(strs: List[str]) -> int:
    strs_len = len(strs)
    if strs_len == 0:
        return 0

    # All strings have the same length, per constraints
    word_len = len(strs[0])

    # Initialize Union-Find with n elements, one for each string.
    # The initial count is n (each string is its own group).
    uf = DisjointSetUnion(strs_len)

    def is_similar(s1: str, s2: str) -> bool:
        """
        Checks if two strings are similar.
        Similar means identical (0 diffs) or 1 swap (2 diffs).
        """
        diff_count = 0
        positions_that_differ = []
        for k in range(word_len):
            if s1[k] != s2[k]:
                positions_that_differ.append(k)
                diff_count += 1

            # Optimization: If more than 2 differences,
            # they can't be similar.
            if diff_count > 2:
                return False

        if diff_count == 2:
            i = positions_that_differ[0]
            j = positions_that_differ[1]
            return s1[i] == s2[j] and s1[j] == s2[i]

        # At this point, diff_count is either 0 or 1
        # Only 0 differences (identical strings) are similar
        return diff_count == 0

    # Iterate over all unique pairs of strings
    for i in range(strs_len):
        for j in range(i + 1, strs_len):
            # If the strings are similar, merge their groups.
            # The union() method handles decrementing the count
            # only if they were in different groups.
            if is_similar(strs[i], strs[j]):
                uf.union(i, j)

    # The final count of disjoint sets is the number of groups
    return uf.get_count()


# Helper: Decide if two strings are similar
def are_similar(s1, s2):
    diff = []
    for a, b in zip(s1, s2):
        if a != b:
            diff.append((a, b))
            if len(diff) > 2:
                return False

    return (len(diff) == 0) or (len(diff) == 2 and diff[0] == diff[1][::-1])


def num_similar_groups_2(strs: List[str]) -> int:
    n = len(strs)
    if n == 0:
        return 0

    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if are_similar(strs[i], strs[j]):
                uf.union(i, j)

    roots = {uf.find(i) for i in range(n)}
    return len(roots)
