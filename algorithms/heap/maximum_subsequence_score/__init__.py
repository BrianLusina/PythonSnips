from typing import List
from heapq import heappush, heappop
from operator import itemgetter


def max_score(nums1: List[int], nums2: List[int], k: int) -> int:
    result, total_sum, min_heap = 0, 0, []
    merged = sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True)

    for num_1_value, max_of_2 in merged:
        total_sum += num_1_value
        heappush(min_heap, num_1_value)
        if len(min_heap) == k:
            result = max(result, total_sum * max_of_2)
            total_sum -= heappop(min_heap)

    return result
