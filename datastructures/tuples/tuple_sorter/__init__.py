from operator import itemgetter


def sorter(*params):
    """
    We use itemgetter to enable multiple sort keys.
    """
    return sorted(params, key=itemgetter(0, 1, 2))
