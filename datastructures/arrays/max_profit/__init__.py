from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit that can be made from buying and selling a stock once
    """
    if prices is None or len(prices) < 2:
        return 0

    min_price = prices[0]
    current_max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > current_max_profit:
            current_max_profit = price - min_price

    return current_max_profit
