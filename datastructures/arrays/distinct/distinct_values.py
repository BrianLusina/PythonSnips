def distinct(collection: list) -> int:
    """
    Checks for the distinct values in a collection and returns the count
    Performs operation in nO(nlogn) time
    :param collection: Collection of values
    :returns number of distinct values in the collection
    """
    length = len(collection)

    if length == 0:
        return 0

    # performs operation in O(nlogn)
    collection.sort()
    result = 1

    for x in range(1, length):
        if collection[x - 1] != collection[x]:
            result += 1

    return result
