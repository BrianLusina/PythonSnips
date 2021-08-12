"""
Implementation for an even better grouper

This uses inbuilt zip and iter to create an iteration over the inputs which reduces the consumption of memory

Testing this script:
/usr/bin/time -f "Memory used(KB): %M\nUsed Time: (seconds): %U" python better_grouper.py
Memory used(KB): 4553416
Used Time: (seconds): 3.69
"""


def better_grouper(inputs, n):
    """
    This is used to group the numbers (inputs) into groups of 2.
    :param: inputs List of integers
    :param: n Integer used to group the list
    :rtype: list
    """
    iters = [iter(inputs)] * n
    return list(zip(*iters))


for _ in better_grouper(range(100000000), 10):
    pass
