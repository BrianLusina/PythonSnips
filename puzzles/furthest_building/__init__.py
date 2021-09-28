from heapq import heappush, heappop
from typing import List


def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    if len(heights) == 0:
        return 0
    heap = []
    for idx in range(len(heights) - 1):
        next_building = heights[idx + 1]
        current = heights[idx]
        diff = next_building - current

        if diff > 0:
            heappush(heap, diff)
        if len(heap) > ladders:
            bricks -= heappop(heap)

        if bricks < 0:
            return idx
    return len(heights) - 1
