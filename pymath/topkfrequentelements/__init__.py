import random
from collections import Counter
from typing import List

from datastructures.trees.heaps.binary.min_heap import MinHeap


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


def top_k_frequent_with_quick_select(nums: List[int], k: int) -> List[int]:
    """
    Uses Quickselect algorithm to find the top k most frequent elements in the list of integers.
    https://en.wikipedia.org/wiki/Quickselect

    Complexity Analysi:
    Time complexity: O(N) in the average case, O(N^2) in the worst case. Master Theorem helps to get an average
    complexity by writing the algorithm cost as T(N)=aT(N/b)+f(N). Here we have an example of Master Theorem case III:
    T(N)=T(N/2)+N that results in O(N) time complexity. That's the case of random pivots.

    In the worst-case of constantly bad chosen pivots, the problem is not divided by half at each step, it becomes just
    one element less, that leads to O(N^2) time complexity. It happens, for example, if at each step you choose the
    pivot not randomly, but take the rightmost element. For the random pivot choice the probability of having such a
    worst-case is negligibly small.

    Space complexity: up to O(N) to store hash map and array of unique elements.

    @param nums: list of numbers
    @param k: counter
    @return: top k most frequent elements
    """

    # Space complexity: O(n)
    hash_map = Counter(nums)

    # Space complexity: O(n)
    unique = list(hash_map.keys())

    def partition(left: int, right: int, pivot_index: int) -> int:
        """
        Uses Lomuto Partition scheme to find the pivot index in the array
        https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
        @param left: low index
        @param right: high index
        @param pivot_index: randomly selected index
        @return: pivot index to use in array
        """
        pivot_frequency = hash_map[unique[pivot_index]]

        # 1. move pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        # 2. move all less frequent elements to the left
        store_index = left

        for i in range(left, right):
            if hash_map[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # 3. move pivot to its final place
        unique[right], unique[store_index] = unique[store_index], unique[right]

        return store_index

    def quickselect(left: int, right: int, k_smallest: int) -> None:
        # base case the list contains only 1 element
        if left == right:
            return

        random_pivot_index = random.randint(left, right)

        pivot_index = partition(left, right, random_pivot_index)

        # if the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return
        # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index + 1, right, k_smallest)

    n = len(unique)
    # kth top frequent element is (n - k)th less frequent.
    # Do a partial sort: from less frequent to the most frequent, till
    # (n - k)th less frequent element takes its place (n - k) in a sorted array.
    # All element on the left are less frequent.
    # All the elements on the right are more frequent.
    quickselect(0, n - 1, n - k)

    return unique[n - k:]
