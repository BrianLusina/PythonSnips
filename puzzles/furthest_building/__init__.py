from heapq import heappush, heappop
from typing import List


def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    """
    Returns the index of the furthest building that one can scale using bricks and ladders.

    Uses a Heap to determine this.

    Algorithm:
    heap/priority queue will store k height difference that we need to use ladders.
    Each move, if the height difference diff > 0, we push diff into the heap/priority queue.
    If the size of heap/queue exceed ladders, it means we have to use bricks for one move.
    Then we pop out the smallest difference, and reduce bricks.
    If bricks < 0, we can't make this move, then we return current index idx.
    If we can reach the last building, we return length of heights - 1.

    Complexity:
        Time O(NlogK)
        Space O(K)

    @param heights: Heights of the buildings
    @param bricks: number of bricks
    @param ladders: number of ladders
    @return: index of the furthest building
    """
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
