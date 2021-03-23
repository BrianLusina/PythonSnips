from random import choice


def coin_flip(n):
    """
    Counts the number of occurrences of heads and tails from a coin flip
    A number is input with the number of times a coin is flipped
    To count the number of heads and tails a random generator is used to determine if a coin flip is heads or tails
    a tail counter and head counter will be incremented as a result
    :param n: Number of times a coin is flipped
    :return: a dictionary with the number of tails and heads
    :raises: TypeError, if the input is invalid, will only accept int inputs
    :rtype: dict
    """

    # check for valid input, raise error if input is not an integer
    if n is None or not isinstance(n, int):
        raise TypeError("Expect integer inputs, instead got {}".format(str(n)))

    # create a coin which will have heads and tails
    COIN = ["T", "H"]

    # create store for the heads and tails count
    result = {"HEADS": 0, "TAILS": 0}

    # in order to get the number of times a coin lands on heads or tails we will need a random generator
    # this will pick between heads or tails
    coin_flips = 0

    while coin_flips < n:
        if choice(COIN) == "T":
            result["TAILS"] += 1
        else:
            result["HEADS"] += 1
        coin_flips += 1

    return result
