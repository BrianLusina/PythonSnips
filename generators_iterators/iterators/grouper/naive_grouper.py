"""
This is used to demonstrate a slow, memory consumption approach to subdividing a group of numbers into groups
of n.
To test this script on a UNIX system, run the script as below
$ /usr/bin/time -f "Memory Used (kB): %M\nUsed Time: (seconds): %U"python naive_grouper.py
"""


def naive_grouper(inputs, n):
    """
    This groups the inputs list of numbers into groups of n.
    :param: inputs List of numbers
    :param: n Integer used to group the list of numbers
    :return: list with tuples of the groupings
    :rtype: list
    """
    num_of_groups = len(inputs) // n
    return [tuple(inputs[i * n: (i + 1) * n]) for i in range(num_of_groups)]


for _ in naive_grouper(range(1000000000), 10):
    pass
