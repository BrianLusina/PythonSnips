from typing import List
from heapq import heapify, heappop, heappush


def total_cost(costs: List[int], k: int, candidates: int) -> int:
    # head_workers stores the first k workers
    head_workers = costs[:candidates]
    # tail_workers stores at most last k workers without any workers from the first k workers
    tail_workers = costs[max(candidates, len(costs) - candidates) :]
    heapify(head_workers)
    heapify(tail_workers)

    # next_head stores the index of the next worker to be added to the head_workers in case of a hire from the head_workers
    next_head = candidates

    # next_tail stores the index of the next worker to be added to the tail_workers in case of a hire from the tail_workers
    next_tail = len(costs) - 1 - candidates

    result = 0

    for _ in range(k):
        if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
            result += heappop(head_workers)

            # only refill queue if there are workers outside the two queues
            if next_head <= next_tail:
                heappush(head_workers, costs[next_head])
                next_head += 1
        else:
            result += heappop(tail_workers)

            # only refill queue if there are workers outside the two queues
            if next_head <= next_tail:
                heappush(tail_workers, costs[next_tail])
                next_tail -= 1

    return result
