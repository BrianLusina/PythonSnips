from collections import Counter
from typing import List


def highest_rank(arr: List[int]) -> int:
    """
    Given an array of integers, find the highest rank number and return it. If there are 2 numbers with the same count.
    Return the one with the highest value.
    @param arr: list of integers
    @return: integer with the most occurrences
    """
    if arr:
        nums = Counter(arr).most_common()
        max_key, max_rank = 0, 0

        for num in nums:
            rank = num[1]
            val = num[0]

            if rank > max_rank or (rank == max_rank and val > max_key):
                max_key, max_rank = val, rank

        return max_key
