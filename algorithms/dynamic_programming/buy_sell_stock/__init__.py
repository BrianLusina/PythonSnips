import math
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit that can be made from buying and selling a stock once

    Time complexity is O(n) as we iterate through each price to get the maximum profit
    Space complexity is O(1) as no extra space is used
    Args:
        prices(list): list of prices
    Returns:
        int: maximum profit that can be made
    """
    if prices is None or len(prices) < 2:
        return 0

    start_price = prices[0]
    current_max_profit = 0

    for price in prices[1:]:
        start_price = min(start_price, price)
        current_max_profit = max(current_max_profit, price - start_price)

    return current_max_profit


def max_profit_two_pointers(prices: List[int]) -> int:
    """
    Variation of max_profit using 2 pointers
    Complexity Analysis:
    Space: O(1), no extra memory is used
    Time: O(n), where n is the size of the input list & we iterate through the list only once
    """
    if prices is None or len(prices) < 2:
        return 0

    number_of_prices = len(prices)

    left, right = 0, 1

    left, right = 0, 1
    current_max_profit = 0

    while right < number_of_prices:
        low = prices[left]
        high = prices[right]

        if low < high:
            profit = high - low
            current_max_profit = max(current_max_profit, profit)
        else:
            # We shift the left pointer to the right pointers position because at this point we know the right pointer
            # is at the lowest possible profit, shifting left by 1 will always give us negative profit. However,
            # shifting it to where the right pointer is will give us the next potential profit to find
            left = right
        right += 1
    return current_max_profit


def max_profit_2(prices: List[int]) -> int:
    if prices is None or len(prices) < 2:
        return 0
    left, right = 0, 1
    current_profit = 0

    while right < len(prices):
        previous_price = prices[left]
        next_price = prices[right]

        if previous_price < next_price:
            profit = next_price - previous_price
            current_profit += profit
        left += 1
        right += 1
    return current_profit


def max_profit_3(prices: List[int]) -> int:
    number_of_prices = len(prices)

    if not prices or number_of_prices < 2:
        return 0

    forward_profit, backward_profit = [0] * number_of_prices, [0] * number_of_prices
    earliest_price = prices[0]

    for day in range(1, number_of_prices):
        earliest_price = min(prices[day], earliest_price)
        forward_profit[day] = max(forward_profit[day - 1], prices[day] - earliest_price)

    latest_price = prices[-1]
    for day in range(number_of_prices - 2, -1, -1):
        latest_price = max(latest_price, prices[day])
        backward_profit[day] = max(backward_profit[day + 1], latest_price - prices[day])

    profit = 0
    for day in range(number_of_prices):
        profit = max(profit, forward_profit[day] + backward_profit[day])

    return profit


def max_profit_3_state_compressed_dp(prices: List[int]) -> int:
    # t1_cost: minimum price paid for the first buy
    # t2_cost: effective minimum price paid for the second buy
    #          (price reduced by the profit from the first transaction)
    t1_cost, t2_cost = float("inf"), float("inf")

    # t1_profit: maximum profit achievable after the first sell
    # t2_profit: maximum profit achievable after the second sell
    t1_profit, t2_profit = 0, 0

    # Iterate through each day's stock price
    for price in prices:
        # Update the minimum cost of the first buy
        # We always want to buy at the lowest price seen so far
        t1_cost = min(t1_cost, price)

        # Update the maximum profit after the first sell
        # Selling today gives profit = price - t1_cost
        t1_profit = max(t1_profit, price - t1_cost)

        # Update the effective cost of the second buy
        # The profit from the first transaction reduces the net cost
        t2_cost = min(t2_cost, price - t1_profit)

        # Update the maximum profit after the second sell
        # Selling today after the second buy gives total profit
        t2_profit = max(t2_profit, price - t2_cost)

    # t2_profit contains the maximum profit with at most two transactions
    return t2_profit


def max_profit_with_fee(prices: List[int], fee: int) -> int:
    # initially, there is no cash
    initial_cash = -math.inf
    # initial profit is 0
    current_profit = 0

    for price in prices:
        # Maximum cash in hand with shares
        # Either
        # 1. withold prev share in which case your cash in hand will not change,
        # 2. or assume there was no currently bought share but you want to buy it today -
        #         In this case: your current cash in hand with shares will be your previous cash
        #         in hand without shares minus buying price of the share today.
        initial_cash = max(initial_cash, current_profit - price)

        # Maximum cash in hand without shares
        # Either
        # 1. withold money without shares in which case your cash in hand will not change,
        # 2. or assume you previously bought the share and you are going to sell that today -
        #         In this case : your current cash in hand without shares will be your previous cash
        #         in hand with shares plus the current selling price minus transaction fee
        current_profit = max(current_profit, initial_cash + price - fee)

    return current_profit
