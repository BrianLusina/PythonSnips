import math
from typing import List
from heapq import heappush, heappop
from fractions import Fraction


def min_cost_to_hire_workers(quality: List[int], wage: List[int], k: int) -> float:
    result, quality_sum, worker_pool = float(math.inf), 0, []

    wage_to_quality = zip(wage, quality)
    workers = sorted((Fraction(w, q), w, q) for w, q in wage_to_quality)

    for ratio, w, q in workers:
        heappush(worker_pool, -q)
        quality_sum += q

        if len(worker_pool) > k:
            quality_sum += heappop(worker_pool)

        if len(worker_pool) == k:
            result = min(result, ratio * quality_sum)
            quality_sum -= -heappop(worker_pool)

    return float(result)


def min_cost_to_hire_workers_2(quality, wage, k):
    # Step 1: Create a list of tuples with (wage/quality ratio, quality) for each worker
    workers = sorted([(w / q, q) for w, q in zip(wage, quality)])

    heap = []  # A max-heap (using negative values for qualities)
    total_quality = 0  # Sum of the qualities of the selected workers
    min_cost = float("inf")  # Initialize the minimum cost to infinity

    # Step 2: Iterate through each worker sorted by their wage-to-quality ratio
    for ratio, q in workers:
        # Add the worker's quality to the heap (negative to simulate a max-heap)
        heappush(heap, -q)
        total_quality += q  # Add the worker's quality to the total quality

        # Step 3: If we have more than k workers, remove the one with the largest quality
        if len(heap) > k:
            # Remove the largest quality (smallest negative number)
            total_quality += heappop(heap)  # Adding the negative value back

        # Step 4: If we have exactly k workers, calculate the cost
        if len(heap) == k:
            # The cost is the current ratio multiplied by the total quality of k workers
            min_cost = min(min_cost, ratio * total_quality)

    # Step 5: Return the minimum cost found
    return min_cost
