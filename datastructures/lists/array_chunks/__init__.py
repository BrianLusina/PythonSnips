def make_parts(arr, chunk_size):
    """
    Return an array split into even chunk sizes, the remaining part if any, is included into the list
    :param arr: the array to split up
    :param chunk_size: the size to split up the list evenly
    :return: a new list evenly divided into chunk sizes
    :rtype: list
    """
    return [arr[x:x + chunk_size] for x in range(0, len(arr), chunk_size)]


def make_parts_yield(arr, chunk_size):
    """
    uses yield to split up the array into even chunks. This will return a generator object
    :param arr: list to split up into chunks
    :param chunk_size: the size to split up the chunks
    :return: a generator object
    :rtype: object
    """
    for x in range(0, len(arr), chunk_size):
        yield arr[x:x + chunk_size]
