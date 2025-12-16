from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    If sum of gas is less than sum of cost, then there is no way to get through all stations. So while we loop through
    the stations we sum up, so that at the end we can check the sum.
    Otherwise, there must be one unique solution, so the first one I find is the right one. If the tank becomes
    negative, we restart because that can't happen.

    Complexity:
    Time Complexity is O(n) where n is the number of gas stations to go though
    Space Complexity is O(1) as no extra space is required
    Args:
        gas (List): gas stations
        cost (List): cost to move from 1 gas station to the next
    Return:
        (int) start index or -1 if impossible
    """
    if (sum(gas) - sum(cost)) < 0:
        return -1

    gas_tank, start_index = 0, 0

    for i in range(len(gas)):
        gas_tank += gas[i] - cost[i]

        if gas_tank < 0:
            start_index = i + 1
            gas_tank = 0
    return start_index
