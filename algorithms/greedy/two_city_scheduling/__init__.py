from typing import List


def two_city_scheduling(costs: List[List[int]]) -> int:
    if not costs:
        return 0

    # Sort by the relative cost difference of sending someone to city A over city B
    # Negative or small differences appear first
    costs.sort(key=lambda x: x[0] - x[1])

    # This gives us the number of people to send to each city. This is equivalent to len(costs) // 2
    n = len(costs) >> 1

    total_cost = 0

    for i in range(n):
        total_cost += costs[i][0] + costs[i + n][1]

    return total_cost
