from typing import List, Tuple
import heapq


def k_closest_to_origin(points: List[List[int]], k: int) -> List[List[int]]:
    # Max heap will store the top k points closest to the origin in the form (-distance, idx). The distance is negated
    # because in Python, the heapq module uses min-heap by default. Negating values gives us a maximum heap.
    # We store the idx of the point for later retrieval from the points array passed in
    max_heap: List[Tuple[int, int]] = []

    for idx, point in enumerate(points):
        x, y = point
        # calculate the distance for this point from the origin
        distance = x * x + y * y

        # If the contents of the heap are less than the desired top k, then we add the current point's distance and idx
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-distance, idx))
        # We check if the calculated distance of this point is less than the top element in the heap. If this point
        # is closer to the origin that what is at the root of the heap, we pop the root of the heap and add this
        # new distance and index.
        # Note the negation here again to get the actual distance
        elif distance < -max_heap[0][0]:
            heapq.heappushpop(max_heap, (-distance, idx))

    # Return the top k points closest to origin. We use 1 to get the index of the point from the original points list
    # as that is what is stored in the max heap
    return [points[point[1]] for point in max_heap]


def k_closest_to_origin_sorting(points: List[List[int]], k: int) -> List[List[int]]:
    # Sort the points by the distance from the origin. This incurs a cost of O(n log(n)) and space cost of O(n) due to
    # timsort
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    # Retrieve the top k points closest to the origin
    return points[:k]
