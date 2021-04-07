from collections import Counter
from typing import List

from datastructures.trees.heaps.min_heap import MinHeap


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)

    return [x for x, y in counter.most_common(k)]


def top_k_frequent_with_min_heap(nums: List[int], k: int) -> List[int]:
    """
    Uses a Min Heap to get the top k frequent elements
    """
    counter = Counter(nums)
    arr = []

    for num, count in counter.items():
        arr.append([-count, num])

    min_heap = MinHeap(arr)
    ans = []

    for _ in range(k):
        a = min_heap.remove_min()
        ans.append(a[1])

    return ans
