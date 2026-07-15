from typing import List, Tuple
from bisect import bisect_left
import heapq


def find_right_interval_sorting_binary_search(intervals: List[List[int]]) -> List[int]:
    if not intervals:
        return []
    interval_len = len(intervals)
    result = [-1] * interval_len
    sorted_intervals_by_start = sorted(
        (start, idx) for idx, (start, _) in enumerate(intervals)
    )

    for idx, (_, end) in enumerate(intervals):
        j = bisect_left(sorted_intervals_by_start, (end, float("-inf")))
        if j < interval_len:
            result[idx] = sorted_intervals_by_start[j][1]

    return result


def find_right_interval_two_heaps(intervals: List[List[int]]) -> List[int]:
    result = [-1] * len(intervals)

    start_heap: List[Tuple[int, int]] = []
    end_heap: List[Tuple[int, int]] = []

    for i, interval in enumerate(intervals):
        heapq.heappush(start_heap, (interval[0], i))
        heapq.heappush(end_heap, (interval[1], i))

    while end_heap:
        value, index = heapq.heappop(end_heap)

        while start_heap and start_heap[0][0] < value:
            heapq.heappop(start_heap)

        if start_heap:
            result[index] = start_heap[0][1]

    return result
