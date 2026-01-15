from typing import List
from math import ceil
import heapq


def max_score(nums: List[int], k: int) -> int:
    score = 0

    # if there are no elements, just return the score of 0
    if len(nums) == 0:
        return score

    # a heapq provides a in-heap, so we'll have to use negative values to simulate a max-heap
    # Create a max-heap by negating all values (heapq is a min-heap)
    # This allows us to efficiently get the maximum element each time
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    for _ in range(k):
        # Extract the maximum element (most negative in our negated heap)
        current_largest = -heapq.heappop(max_heap)
        score += current_largest
        reduced_value = ceil(current_largest / 3)
        heapq.heappush(max_heap, -reduced_value)

    return score
