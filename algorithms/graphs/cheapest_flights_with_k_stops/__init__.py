from typing import List
from math import inf


def find_cheapest_price(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    prices = [inf] * n
    prices[src] = 0

    for i in range(k + 1):
        temp_prices = prices.copy()

        for source, destination, price in flights:
            if prices[source] == inf:
                continue
            if prices[source] + price < temp_prices[destination]:
                temp_prices[destination] = prices[source] + price
        prices = temp_prices

    return -1 if prices[dst] == inf else prices[dst]
