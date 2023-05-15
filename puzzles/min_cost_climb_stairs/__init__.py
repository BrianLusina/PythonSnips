from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    minimum_cost = [0] * (len(cost) + 1)

    for x in range(2, len(cost) + 1):
        one_step = minimum_cost[x - 1] + cost[x - 1]
        two_steps = minimum_cost[x - 2] + cost[x - 2]
        minimum_cost[x] = min(one_step, two_steps)

    return minimum_cost[-1]
