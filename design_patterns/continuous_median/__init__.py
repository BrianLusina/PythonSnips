from typing import Optional
import heapq


class ContinuousMedianHandler:
    def __init__(self):
        self.median: Optional[int | float] = None
        # Max heap keeps track of the lower half of numbers
        self.max_heap = []
        # Min Heap keeps track of the upper half of numbers
        self.min_heap = []

    def insert(self, number: int) -> None:
        heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -number))

        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        if len(self.max_heap) == len(self.min_heap):
            max_heap_root = self.max_heap[0]
            min_heap_root = self.min_heap[0]
            median = (min_heap_root - max_heap_root) / 2
            self.median = median
        else:
            self.median = self.min_heap[0]

    def get_median(self) -> Optional[int | float]:
        return self.median
