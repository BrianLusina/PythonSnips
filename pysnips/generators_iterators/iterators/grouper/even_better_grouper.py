"""
This improves upon better_grouper in that it accounts for the second input not being divisible or a factor of the
first input list of integers.
This uses the zip_longest module from the itertools module to return all groupings of the inputs list of numbers.
it has the fill_value keyword, which defaults to None to fill the remaining blanks. An example is in the doc_test
"""
from itertools import zip_longest


def even_better_grouper(inputs, n, fillvalue=None):
    """
    Groups the inputs into groups of n
    :param: inputs List of integers
    :param: n Integer
    :param: fillvalue defaults to None, is what is used to 'fill' the remaning spaces of the
    groupings
    :returns: List of tuples with each of length n
    :rtype: list
    """

    iters = [iter(inputs)] * n
    return list(zip_longest(*iters, fillvalue=fillvalue))


for _ in even_better_grouper(range(100000000), 10):
    pass
