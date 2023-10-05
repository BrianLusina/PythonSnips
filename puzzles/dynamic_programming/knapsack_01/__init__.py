from typing import List


def knapsack_01(values: List[int], weights: List[int], capacity: int) -> int:
    values_len = len(values)

    knapsack = [0 for _ in range(capacity + 1)]

    for current_value in range(1, values_len + 1):

        for current_capacity in range(capacity, 0, -1):
            if weights[current_value - 1] <= current_capacity:
                knapsack_at_current_capacity = knapsack[current_capacity]
                previous_knapsack_capacity = knapsack[current_capacity - weights[current_value - 1]]
                value = values[current_value - 1]

                knapsack[current_capacity] = max(knapsack_at_current_capacity, previous_knapsack_capacity + value)

    return knapsack[capacity]
