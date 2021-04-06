"""
Simple demonstration of ordered dict
this will preserver the order in which items are added to dictionary unlike the standard dictionary
"""
from collections import OrderedDict
from string import ascii_lowercase


def map_ascii_to_range(range_length):
    """
    maps ascii letters to a range, where the letters are keys and the values are numbers
    this will produce an output based on the range_length
    :param range_length: length of the range ot use
    :return: dictionary with mapping unordered
    :rtype: dict
    """
    return dict(zip(ascii_lowercase, range(range_length)))


def map_ascii_to_range_ordered(range_length):
    """
    performs the same calculation as above, with difference of ordering the output as it came in
    >>> map_ascii_to_range_ordered(5)
    >>> OrderedDict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)])
    :param range_length: length to use in range
    :return: ordered dictionary
    """
    return OrderedDict(zip(ascii_lowercase, range(range_length)))


if __name__ == "__main__":
    result1 = map_ascii_to_range(5)
    result2 = map_ascii_to_range_ordered(5)

    print(result1)  # {'d': 3, 'e': 4, 'a': 0, 'b': 1, 'c': 2}
    print(result2)  # OrderedDict([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)])
