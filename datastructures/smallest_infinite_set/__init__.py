from typing import Set, List
from heapq import heapify, heappop, heappush


class SmallestInfiniteSet:
    """
    Complexity Analysis

    Here, n is the number of add_back(num) calls and m is the number of pop_smallest() calls

    - Time Complexity O((m+n) * log(n))
        - In each pop_smallest() method call, in the worst case, we will need to remove a number from the hash set which
        will take O(1) time, and the top of the min-heap which will take O(log(n)) time. Thus, for m calls it will take
        O(m * log(n)) time.

        - In each add_back(num) method call, we might push num in the hash set which will take O(1) time and min-heap
        which will take O(log(n)). Thus, for n calls it will take O(n * log(n)) time.

    - Space complexity: O(n)
        - In the worst case, we might add n elements in the hash set and the min-heap. Thus, it will take O(n) space
    """

    def __init__(self):
        # stores the removed numbers added again
        self.elements: Set[int] = set()
        # minimum heap priority queue to store the minimum number of all added numbers on the top
        self.added_elements: List[int] = []
        heapify(self.added_elements)
        # variable initialized to 1 denoting the current minimum value in the set of all positive integers
        self.current_element = 1

    def pop_smallest(self) -> int:
        # if we have elements in the heap, the top element is removed and returned
        if len(self.added_elements) > 0:
            # pop the smallest element
            result = heappop(self.added_elements)
            # remove it from the set
            self.elements.remove(result)
        else:
            # the smallest element is the current element, we return it and set the current element to the next element
            result = self.current_element
            self.current_element += 1
        return result

    def add_back(self, num: int) -> None:
        # if the num is greater than or equal to the current element, it is not added to the set, as it is greater than
        # our current element, this means that in the set of all positive integers, it already exists. Similarly, if it
        # is already in the element set, we do not add it as well as it might have been added before; this could be the
        # case where it is less than the current element.
        if self.current_element <= num or num in self.elements:
            return
        # if not, then this num is smaller than the current element and is also not in the element set, therefore it is
        # added back
        heappush(self.added_elements, num)
        self.elements.add(num)
