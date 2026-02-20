from typing import List, Tuple
import heapq


def min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    query_len=len(queries)

    query_indexes = list(range(query_len))
    query_indexes.sort(key=lambda q: queries[q])

    # Sort intervals in ascending order. Avoiding sorting in place to keep the 'intervals' input without side effects.
    # Space incurred is O(n) where n is the size of intervals and time is O(n log(n))
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    intervals_len = len(sorted_intervals)

    min_heap: List[Tuple[int, int]] = []

    result = [-1] * query_len
    # Pointer to sweep through interval list
    i = 0

    for query_idx in query_indexes:
        query = queries[query_idx]

        # Push all intervals that start at or before query into the heap
        # (they are "eligible" to cover query, but might end before query)
        while i < intervals_len and sorted_intervals[i][0] <= query:
            current_interval = sorted_intervals[i]
            interval_start, interval_end = current_interval
            interval_size = interval_end - interval_start + 1
            heapq.heappush(min_heap, (interval_size, interval_end))
            i += 1

        # Remove intervals that end before q (they can't cover q anymore)
        while min_heap and min_heap[0][1] < query:
            heapq.heappop(min_heap)

        # If heap is not empty, top has the smallest size among intervals that cover q
        if min_heap:
            result[query_idx] = min_heap[0][0]

    return result
