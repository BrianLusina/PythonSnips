def array_pair_sum(k, array):
    """
    Iterative method
    Loops through the array, checking if a pair sums up to the value k
    Returns all pairs that sum up to k
    complexity: O(n^2)
    :param k: The value to check sum of pairs agains
    :param array: The array of integers to loop through
    :return: The sum of pairs
    :rtype: list
    """
    result = []
    for x in range(len(array)):
        for y in range(x + 1, len(array)):
            if array[x] + array[y] == k:
                result.append([array[x], array[y]])

    return result
