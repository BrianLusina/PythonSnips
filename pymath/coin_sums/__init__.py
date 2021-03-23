def make_pounds(coins, bill):
    """
    Find how many ways there are to make bill from the given list of coins
    :param coins List of coins
    :type coins list
    :param bill Coin/note to make change for
    :type bill int
    :return: Number of ways to make change for the given currency
    :rtype: int
    """
    ways_to_make_bill = [0] * (bill + 1)
    ways_to_make_bill[0] = 1

    for x in range(len(coins)):
        for n in range(coins[x], bill + 1):
            ways_to_make_bill[n] += ways_to_make_bill[n - coins[x]]

    return ways_to_make_bill[bill]


if __name__ == "__main__":
    c = [1, 2, 5, 10, 20, 50, 100, 200]
    b = 200
    ways_to_make_b = make_pounds(c, b)
    print(f"There are {ways_to_make_b} ways to make change for {b} given {c}")
