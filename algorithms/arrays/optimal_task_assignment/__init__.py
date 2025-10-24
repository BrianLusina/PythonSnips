from typing import List, Tuple


def optimal_task_assignment(tasks: List[int]) -> List[Tuple[int, int]]:
    """
    After sorting the array, the for loop iterates for half the length of the array adds the pairs using indexing to a
    list. So ~x is the bitwise complement operator which puts a negative sign in front of x and subtracts 1 from it.
    Thus, the negative numbers as indexes mean that you count from the right of the array instead of the left. So,
    numbers[-1] refers to the last element, numbers[-2] is the second-last, and so on. In this way, we are able to pair
    the numbers from the beginning of the array to the end of the array.
    """
    sorted_tasks = sorted(tasks)
    result: List[Tuple[int, int]] = []

    for x in range(len(sorted_tasks) // 2):
        result.append((sorted_tasks[x], sorted_tasks[~x]))

    return result
