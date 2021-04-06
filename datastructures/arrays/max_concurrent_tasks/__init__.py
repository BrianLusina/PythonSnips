# from datastructures.trees.heaps.min_heap import MinHeap
from typing import List

from datastructures.queues.priority import PriorityQueue


# TODO: does not work for edge cases where 2 tasks have the same start and end time
def find_max_concurrent_tasks(tasks: List[List]) -> int:
    tasks.sort(key=lambda i: i[0])

    # min_heap = MinHeap()
    pq = PriorityQueue()

    # Add first task end time
    pq.add(tasks[0][1])
    # min_heap.insert(tasks[0][1])

    for task in tasks:
        # remove all tasks that end before current task
        while not pq.is_empty() and task[0] >= pq.peek():
            pq.poll()
            # min_heap.remove_min()

        # add current task end time
        pq.add(task[1])
        # min_heap.insert(task[1])

    return pq.size
    # return min_heap.size()
