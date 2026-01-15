from typing import List
import heapq


def k_closest(nums: List[int], k: int, target: int):
    heap = []

    for num in nums:
        diff = abs(num - target)

        if len(heap) < k:
            heapq.heappush(heap, (-diff, num))
        elif diff < -heap[0][0]:
            heapq.heappushpop(heap, (-diff, num))

    distances = [pair[1] for pair in heap]
    distances.sort()
    return distances
