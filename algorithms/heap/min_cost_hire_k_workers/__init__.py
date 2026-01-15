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
