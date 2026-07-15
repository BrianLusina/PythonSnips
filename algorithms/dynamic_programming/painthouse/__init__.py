from typing import List


def min_cost_to_paint_houses_alternate_colors(costs: List[List[int]]) -> int:
    """
    Finds the minimum cost to paint houses in a street without repeating colors consecutively
    Args:
        costs(list): Costs of painting houses as a 2D list
    Returns:
        int: minimum cost of painting houses
    """
    # If there are no costs of painting the houses, then the minimum cost is 0
    if not costs:
        return 0

    # initially, the cost of painting any house any color is 0
    # Initialize minimum costs for painting up to previous house with each color
    # prev_min_cost_red: min cost if previous house painted red
    # prev_min_cost_blue: min cost if previous house painted blue
    # prev_min_cost_green: min cost if previous house painted green
    prev_min_cost_red = 0
    prev_min_cost_blue = 0
    prev_min_cost_green = 0

    # Iterate through each house cost
    for current_cost in costs:
        cost_red, cost_blue, cost_green = current_cost

        # Calculate minimum cost for current house with each color
        # Current house painted red: add red cost to min of (prev blue, prev green)
        # Current house painted blue: add blue cost to min of (prev red, prev green)
        # Current house painted green: add green cost to min of (prev red, prev blue)
        curr_min_cost_red = min(prev_min_cost_blue, prev_min_cost_green) + cost_red
        curr_min_cost_blue = min(prev_min_cost_red, prev_min_cost_green) + cost_blue
        curr_min_cost_green = min(prev_min_cost_red, prev_min_cost_blue) + cost_green

        # Update previous costs for next iteration
        prev_min_cost_red = curr_min_cost_red
        prev_min_cost_blue = curr_min_cost_blue
        prev_min_cost_green = curr_min_cost_green

    # Return minimum cost among all three color options for the last house
    return min(prev_min_cost_red, prev_min_cost_blue, prev_min_cost_green)
